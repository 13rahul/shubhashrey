<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed.']);
    exit;
}

require_once dirname(__DIR__) . '/includes/bootstrap.php';

$raw = file_get_contents('php://input');
$data = json_decode($raw ?: '', true);
if (!is_array($data)) {
    // Also accept classic form posts
    $data = $_POST;
}

$source = strtolower(trim((string) ($data['source'] ?? 'contact')));
if (!in_array($source, ['contact', 'distributor'], true)) {
    $source = 'contact';
}

$name = trim((string) ($data['name'] ?? ''));
if ($name === '') {
    $first = trim((string) ($data['firstName'] ?? ''));
    $last = trim((string) ($data['lastName'] ?? ''));
    $name = trim($first . ' ' . $last);
}
if ($name === '') {
    $name = trim((string) ($data['fullName'] ?? ''));
}

$email = trim((string) ($data['email'] ?? ''));
$phone = trim((string) ($data['phone'] ?? ''));
$company = trim((string) ($data['company'] ?? ''));
$city = trim((string) ($data['city'] ?? ''));
$district = trim((string) ($data['district'] ?? ''));
$state = trim((string) ($data['state'] ?? ''));
$midc = trim((string) ($data['midc'] ?? ''));
$territory = trim((string) ($data['territory'] ?? ($data['area'] ?? '')));
$businessType = trim((string) ($data['business_type'] ?? ($data['businessType'] ?? '')));
$interest = trim((string) ($data['interest'] ?? ''));
$message = trim((string) ($data['message'] ?? ''));
$experience = trim((string) ($data['experience'] ?? ''));

if ($experience !== '') {
    $message = ($message !== '' ? $message . "\n\n" : '') . 'Experience: ' . $experience;
}

// Website forms can omit email for rare cases — keep validation for public API
if ($name === '' || $email === '' || $message === '') {
    http_response_code(422);
    echo json_encode(['success' => false, 'message' => 'Name, email, and message are required.']);
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['success' => false, 'message' => 'Please enter a valid email address.']);
    exit;
}

$channelNote = $source === 'distributor'
    ? 'Inbound lead — Become a Distributor form'
    : 'Inbound lead — Contact Us form';

try {
    $id = shubh_lead_create([
        'source' => $source,
        'lead_label' => 'Inbound',
        'name' => $name,
        'email' => $email,
        'phone' => $phone,
        'company' => $company,
        'city' => $city,
        'district' => $district,
        'state' => $state,
        'midc' => $midc,
        'territory' => $territory,
        'business_type' => $businessType,
        'interest' => $interest,
        'message' => $message,
        'status' => 'new',
        'notes' => $channelNote . ' · ' . date('Y-m-d H:i'),
    ]);

    echo json_encode([
        'success' => true,
        'message' => 'Inbound lead saved.',
        'id' => $id,
        'lead_label' => 'Inbound',
    ]);
} catch (Throwable $e) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'message' => 'Could not save lead. Please try WhatsApp or call us.',
    ]);
}
