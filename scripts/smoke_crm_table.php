<?php
declare(strict_types=1);
require __DIR__ . '/../includes/bootstrap.php';

$id = shubh_lead_create([
    'source' => 'manual',
    'name' => 'Bhosari Fab Test',
    'company' => 'Test Fab Pvt Ltd',
    'phone' => '9876500001',
    'email' => 'fab@example.com',
    'city' => 'Pune',
    'district' => 'Pune',
    'state' => 'Maharashtra',
    'midc' => 'Bhosari MIDC',
    'interest' => 'E7018',
    'message' => 'Need electrodes',
    'notes' => 'Initial visit',
]);
echo "created={$id}\n";

shubh_lead_update($id, [
    'source' => 'visit',
    'name' => 'Bhosari Fab Test',
    'company' => 'Test Fab Pvt Ltd',
    'phone' => '9876500001',
    'email' => 'fab@example.com',
    'city' => 'Pune',
    'district' => 'Pune',
    'state' => 'Maharashtra',
    'midc' => 'Bhosari MIDC',
    'interest' => 'E7018;E6013',
    'message' => 'Need electrodes',
    'notes' => 'Initial visit',
    'status' => 'contacted',
]);
shubh_lead_append_note($id, 'Follow-up scheduled');

$row = shubh_db()->query('SELECT * FROM leads WHERE id=' . (int) $id)->fetch();
echo "midc={$row['midc']}\ndistrict={$row['district']}\nstatus={$row['status']}\n";
echo "notes_has_followup=" . (str_contains((string) $row['notes'], 'Follow-up') ? '1' : '0') . "\n";
echo "cols_ok=" . (isset($row['district'], $row['midc']) ? '1' : '0') . "\n";
