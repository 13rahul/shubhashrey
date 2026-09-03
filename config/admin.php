<?php
/**
 * Admin CRM config — change password after first login via admin UI or by updating this hash.
 * Default login: admin@shubhshrey.com / ChangeMe@2026
 */
declare(strict_types=1);

return [
    'site_name' => 'Shubhshrey Industries',
    'admin_email' => 'admin@shubhshrey.com',
    // password_hash('ChangeMe@2026', PASSWORD_DEFAULT)
    'admin_password_hash' => '$2y$10$R8Rk50mDCeJixyCb7wKOWuYjPJa7ECwRFpLDYzestFDUiEkVsTkCC',
    'session_name' => 'shubhshrey_admin',
];
