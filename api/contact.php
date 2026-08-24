<?php
header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed.']);
    exit;
}

$raw = file_get_contents('php://input');
$data = json_decode($raw, true);

if (!is_array($data)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Invalid request body.']);
    exit;
}

$firstName = trim((string)($data['firstName'] ?? ''));
$lastName  = trim((string)($data['lastName'] ?? ''));
$email     = trim((string)($data['email'] ?? ''));
$phone     = trim((string)($data['phone'] ?? ''));
$message   = trim((string)($data['message'] ?? ''));

if ($firstName === '' || $lastName === '' || $email === '' || $message === '') {
    http_response_code(422);
    echo json_encode(['success' => false, 'message' => 'Please fill all required fields.']);
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['success' => false, 'message' => 'Please enter a valid email address.']);
    exit;
}

$to = 'contact@shubhshrey.com';
$subject = 'Website contact from ' . $firstName . ' ' . $lastName;
$body = "New contact form submission\n\n"
    . "Name: {$firstName} {$lastName}\n"
    . "Email: {$email}\n"
    . "Phone: {$phone}\n\n"
    . "Message:\n{$message}\n";

$headers = [
    'From: website@shubhshrey.com',
    'Reply-To: ' . $email,
    'Content-Type: text/plain; charset=UTF-8',
    'X-Mailer: PHP/' . phpversion(),
];

$sent = @mail($to, $subject, $body, implode("\r\n", $headers));

if (!$sent) {
    // Log locally so XAMPP setups without SMTP still capture messages
    $logDir = __DIR__ . '/../storage';
    if (!is_dir($logDir)) {
        @mkdir($logDir, 0755, true);
    }
    $logFile = $logDir . '/contact-log.txt';
    $entry = "==== " . date('c') . " ====\n" . $body . "\n";
    @file_put_contents($logFile, $entry, FILE_APPEND);

    echo json_encode([
        'success' => true,
        'message' => 'Message saved. We will follow up soon.',
        'note' => 'Mail transport unavailable locally; message logged to storage/contact-log.txt',
    ]);
    exit;
}

echo json_encode(['success' => true, 'message' => 'Message sent.']);
