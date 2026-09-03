<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/includes/bootstrap.php';
shubh_require_admin();
header('Location: leads.php');
exit;
