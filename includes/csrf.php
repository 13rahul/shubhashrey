<?php
declare(strict_types=1);

function shubh_csrf_token(): string
{
    if (empty($_SESSION['csrf_token']) || !is_string($_SESSION['csrf_token'])) {
        $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
    }
    return $_SESSION['csrf_token'];
}

function shubh_csrf_field(): string
{
    return '<input type="hidden" name="csrf_token" value="' . shubh_h(shubh_csrf_token()) . '">';
}

function shubh_csrf_verify(?string $token): void
{
    $session = $_SESSION['csrf_token'] ?? '';
    if (!is_string($token) || $token === '' || !is_string($session) || !hash_equals($session, $token)) {
        throw new RuntimeException('Invalid security token. Please refresh and try again.');
    }
}
