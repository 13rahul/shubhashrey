<?php
declare(strict_types=1);

/**
 * Shared bootstrap for admin + API.
 */

if (session_status() === PHP_SESSION_NONE) {
    $configPreview = require dirname(__DIR__) . '/config/admin.php';
    session_name($configPreview['session_name'] ?? 'shubhshrey_admin');
    session_start([
        'cookie_httponly' => true,
        'cookie_samesite' => 'Lax',
        'use_strict_mode' => true,
    ]);
}

define('SHUBH_ROOT', dirname(__DIR__));
define('SHUBH_STORAGE', SHUBH_ROOT . '/storage');
define('SHUBH_CONFIG', SHUBH_ROOT . '/config/admin.php');

function shubh_config(): array
{
    static $config;
    if ($config === null) {
        $config = require SHUBH_CONFIG;
    }
    return $config;
}

function shubh_h(?string $value): string
{
    return htmlspecialchars((string) $value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

require_once __DIR__ . '/csrf.php';
require_once __DIR__ . '/db.php';
require_once __DIR__ . '/auth.php';
