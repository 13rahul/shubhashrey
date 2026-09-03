<?php
declare(strict_types=1);

require __DIR__ . '/../includes/bootstrap.php';

echo "pdo_ok=" . (shubh_db() instanceof PDO ? "1" : "0") . PHP_EOL;

$id = shubh_lead_create([
    'source' => 'contact',
    'name' => 'Test Lead',
    'email' => 'test@example.com',
    'phone' => '9876543210',
    'message' => 'Smoke test lead',
    'status' => 'new',
]);
echo "lead_id={$id}" . PHP_EOL;

$ok = shubh_attempt_login('admin@shubhshrey.com', 'ChangeMe@2026');
echo "login_ok=" . ($ok ? "1" : "0") . PHP_EOL;

$bad = shubh_attempt_login('admin@shubhshrey.com', 'wrong');
echo "bad_login=" . ($bad ? "1" : "0") . PHP_EOL;

$n = (int) shubh_db()->query('SELECT COUNT(*) FROM leads')->fetchColumn();
echo "lead_count={$n}" . PHP_EOL;

$stmt = shubh_db()->prepare('UPDATE leads SET status = :s, updated_at = :u WHERE id = :id');
$stmt->execute([':s' => 'contacted', ':u' => date('c'), ':id' => $id]);
$row = shubh_db()->query('SELECT status FROM leads WHERE id = ' . (int) $id)->fetch();
echo "status_update=" . ($row['status'] ?? '') . PHP_EOL;

echo "sqlite=" . (is_file(SHUBH_STORAGE . '/crm.sqlite') ? "1" : "0") . PHP_EOL;
