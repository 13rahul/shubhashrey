<?php
/**
 * Import Bhosari MIDC prospect CSV into CRM leads (SQLite).
 *
 * Usage:
 *   php scripts/import_bhosari_to_crm.php
 *   php scripts/import_bhosari_to_crm.php --replace-tests
 */
declare(strict_types=1);

require_once dirname(__DIR__) . '/includes/bootstrap.php';

$csvPath = dirname(__DIR__) . '/data/bhosari-midc-prospects.csv';
if (!is_readable($csvPath)) {
    fwrite(STDERR, "Missing CSV: {$csvPath}\n");
    exit(1);
}

$replaceTests = in_array('--replace-tests', $argv, true);
$pdo = shubh_db();

if ($replaceTests) {
    // Remove obvious smoke-test rows only
    $pdo->exec(
        "DELETE FROM leads WHERE
            (name IN ('Test Lead', 'Bhosari Fab Test') AND source IN ('contact', 'visit'))
            OR company = 'Test Fab Pvt Ltd'"
    );
    echo "Removed smoke-test leads.\n";
}

$fh = fopen($csvPath, 'rb');
if ($fh === false) {
    fwrite(STDERR, "Cannot open CSV\n");
    exit(1);
}
$header = fgetcsv($fh);
if (!is_array($header)) {
    fwrite(STDERR, "Empty CSV\n");
    exit(1);
}
$header = array_map(static fn($h) => trim((string) $h), $header);

$existing = [];
foreach ($pdo->query('SELECT id, company, phone, name FROM leads') as $row) {
    $key = strtolower(trim((string) $row['company']));
    if ($key !== '') {
        $existing[$key] = (int) $row['id'];
    }
}

$inserted = 0;
$skipped = 0;
$updated = 0;

while (($cols = fgetcsv($fh)) !== false) {
    if (count($cols) < 3) {
        continue;
    }
    $row = [];
    foreach ($header as $i => $key) {
        $row[$key] = trim((string) ($cols[$i] ?? ''));
    }

    $company = $row['company_name'] ?? '';
    if ($company === '') {
        continue;
    }

    $contact = $row['contact_person_name'] ?? '';
    $name = $contact !== '' ? $contact : $company;
    $phone = $row['phone_primary'] ?? '';
    $email = $row['email'] ?? '';
    $plant = $row['plant_name'] ?? ($row['area_block'] ?? '');
    $products = $row['products_services'] ?? '';
    $address = $row['plot_address'] ?? '';
    $industry = $row['industry_category'] ?? '';
    $electrodes = $row['electrode_likely'] ?? '';
    $pitch = $row['pitch_angle'] ?? '';
    $priority = $row['priority_label'] ?? '';
    $website = $row['website'] ?? '';
    $notesExtra = $row['notes'] ?? '';
    $companyId = $row['company_id'] ?? '';

    $notesParts = array_filter([
        $companyId !== '' ? "Prospect ID: {$companyId}" : '',
        $priority !== '' ? "Priority: {$priority}" : '',
        $plant !== '' ? "Plant: {$plant}" : '',
        $address !== '' ? "Address: {$address}" : '',
        $products !== '' ? "Products/Services: {$products}" : '',
        $pitch !== '' ? "Pitch: {$pitch}" : '',
        $website !== '' ? "Website: {$website}" : '',
        $notesExtra !== '' ? $notesExtra : '',
    ]);

    $payload = [
        'source' => 'visit',
        'name' => $name,
        'email' => $email,
        'phone' => $phone,
        'company' => $company,
        'city' => 'Bhosari',
        'district' => 'Pune',
        'state' => 'Maharashtra',
        'midc' => 'Bhosari MIDC',
        'territory' => $plant !== '' ? $plant : 'Bhosari MIDC',
        'business_type' => $industry,
        'interest' => $electrodes,
        'message' => $products,
        'status' => 'new',
        'notes' => implode("\n", $notesParts),
    ];

    $key = strtolower($company);
    if (isset($existing[$key])) {
        // Refresh enrichment on existing Bhosari import (same company name)
        shubh_lead_update($existing[$key], $payload);
        $updated++;
        continue;
    }

    $id = shubh_lead_create($payload);
    $existing[$key] = $id;
    $inserted++;
}

fclose($fh);

$total = (int) $pdo->query('SELECT COUNT(*) FROM leads')->fetchColumn();
echo "Inserted: {$inserted}\n";
echo "Updated: {$updated}\n";
echo "Skipped: {$skipped}\n";
echo "CRM leads total: {$total}\n";
echo "Open: admin/leads.php\n";
