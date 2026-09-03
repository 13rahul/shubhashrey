<?php
declare(strict_types=1);

function shubh_admin_logged_in(): bool
{
    return !empty($_SESSION['admin_logged_in']) && $_SESSION['admin_logged_in'] === true;
}

function shubh_require_admin(): void
{
    if (!shubh_admin_logged_in()) {
        header('Location: login.php');
        exit;
    }
}

function shubh_attempt_login(string $email, string $password): bool
{
    $config = shubh_config();
    $expectedEmail = strtolower(trim((string) ($config['admin_email'] ?? '')));
    $hash = (string) ($config['admin_password_hash'] ?? '');

    if ($expectedEmail === '' || $hash === '') {
        return false;
    }

    if (strtolower(trim($email)) !== $expectedEmail) {
        return false;
    }

    if (!password_verify($password, $hash)) {
        return false;
    }

    if (session_status() === PHP_SESSION_ACTIVE && !headers_sent()) {
        session_regenerate_id(true);
    }
    $_SESSION['admin_logged_in'] = true;
    $_SESSION['admin_email'] = $expectedEmail;
    return true;
}

function shubh_logout(): void
{
    $_SESSION = [];
    if (ini_get('session.use_cookies')) {
        $params = session_get_cookie_params();
        setcookie(session_name(), '', time() - 42000, $params['path'], $params['domain'], (bool) $params['secure'], (bool) $params['httponly']);
    }
    session_destroy();
}

function shubh_update_admin_password(string $newPassword): bool
{
    if (strlen($newPassword) < 8) {
        return false;
    }

    $configPath = SHUBH_CONFIG;
    $config = shubh_config();
    $hash = password_hash($newPassword, PASSWORD_DEFAULT);
    $config['admin_password_hash'] = $hash;

    $export = "<?php\ndeclare(strict_types=1);\n\nreturn " . var_export($config, true) . ";\n";
    $ok = file_put_contents($configPath, $export) !== false;
    if ($ok) {
        // Refresh static cache by re-requiring is not possible; next request loads new file.
        // Clear opcache if available.
        if (function_exists('opcache_invalidate')) {
            opcache_invalidate($configPath, true);
        }
    }
    return $ok;
}
