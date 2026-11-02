<?php
/**
 * Live PHP smoke: auth helpers, lead create/update/delete, password verify.
 * Run: php scripts/_crm_php_smoke.php
 */
declare(strict_types=1);

$root = dirname(__DIR__);
require_once $root . '/includes/bootstrap.php';

$failures = 0;
function assert_true(bool $cond, string $msg): void
{
    global $failures;
    if ($cond) {
        echo "OK  {$msg}\n";
    } else {
        echo "FAIL {$msg}\n";
        $failures++;
    }
}

$config = shubh_config();
assert_true(($config['admin_email'] ?? '') === 'admin@shubhshrey.com', 'admin email');
assert_true(
    password_verify('ChangeMe@2026', (string) ($config['admin_password_hash'] ?? '')),
    'default password verifies'
);

// Clean session login
$_SESSION = [];
assert_true(!shubh_admin_logged_in(), 'starts logged out');
assert_true(shubh_attempt_login('admin@shubhshrey.com', 'ChangeMe@2026'), 'login succeeds');
assert_true(shubh_admin_logged_in(), 'session marked logged in');
assert_true(!shubh_attempt_login('admin@shubhshrey.com', 'wrong'), 'bad password rejected');

$id = shubh_lead_create([
    'source' => 'contact',
    'lead_label' => 'Inbound',
    'name' => 'PHP Smoke Contact',
    'email' => 'php.smoke.contact@example.com',
    'phone' => '9111111111',
    'message' => 'php smoke contact',
    'status' => 'new',
    'notes' => 'php smoke',
]);
assert_true($id > 0, "created contact lead #{$id}");

$distId = shubh_lead_create([
    'source' => 'distributor',
    'lead_label' => 'Inbound',
    'name' => 'PHP Smoke Dist',
    'email' => 'php.smoke.dist@example.com',
    'phone' => '9222222222',
    'company' => 'PHP Co',
    'city' => 'Baramati',
    'state' => 'Maharashtra',
    'territory' => 'MIDC',
    'business_type' => 'Dealer',
    'interest' => 'Full range',
    'message' => 'php smoke distributor',
    'status' => 'new',
]);
assert_true($distId > 0, "created distributor lead #{$distId}");

shubh_lead_update($id, [
    'source' => 'contact',
    'lead_label' => 'Inbound',
    'name' => 'PHP Smoke Contact',
    'email' => 'php.smoke.contact@example.com',
    'phone' => '9111111111',
    'message' => 'php smoke contact',
    'status' => 'contacted',
    'notes' => 'php smoke',
]);
shubh_lead_append_note($id, 'Followed up by phone');

$stmt = shubh_db()->prepare('SELECT status, notes, source FROM leads WHERE id = :id');
$stmt->execute([':id' => $id]);
$row = $stmt->fetch();
assert_true(($row['status'] ?? '') === 'contacted', 'status updated to contacted');
assert_true(str_contains((string) ($row['notes'] ?? ''), 'Followed up by phone'), 'note appended');

$stmt = shubh_db()->prepare('SELECT company, territory, source FROM leads WHERE id = :id');
$stmt->execute([':id' => $distId]);
$d = $stmt->fetch();
assert_true(($d['source'] ?? '') === 'distributor' && ($d['company'] ?? '') === 'PHP Co', 'distributor fields persisted');

$del = shubh_db()->prepare('DELETE FROM leads WHERE id IN (:a, :b)');
$del->execute([':a' => $id, ':b' => $distId]);
assert_true(true, 'cleaned smoke leads');

$token = shubh_csrf_token();
assert_true(strlen($token) === 64, 'csrf token generated');
try {
    shubh_csrf_verify($token);
    assert_true(true, 'csrf verify passes');
} catch (Throwable $e) {
    assert_true(false, 'csrf verify failed');
}

shubh_logout();
assert_true(!shubh_admin_logged_in(), 'logout clears session');

echo $failures === 0 ? "\nALL PASSED\n" : "\n{$failures} FAILURE(S)\n";
exit($failures === 0 ? 0 : 1);
