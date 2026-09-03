<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/includes/bootstrap.php';

if (shubh_admin_logged_in()) {
    header('Location: leads.php');
    exit;
}

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        shubh_csrf_verify($_POST['csrf_token'] ?? null);
        $email = trim((string) ($_POST['email'] ?? ''));
        $password = (string) ($_POST['password'] ?? '');
        if ($email === '' || $password === '') {
            throw new RuntimeException('Enter email and password.');
        }
        if (!shubh_attempt_login($email, $password)) {
            throw new RuntimeException('Invalid email or password.');
        }
        header('Location: leads.php');
        exit;
    } catch (Throwable $e) {
        $error = $e->getMessage();
    }
}

$config = shubh_config();
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Admin Login | <?= shubh_h($config['site_name'] ?? 'Shubhshrey') ?></title>
  <link rel="icon" href="../assets/logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/admin.css" />
</head>
<body>
  <div class="login-wrap">
    <div class="login-card">
      <div class="admin-brand" style="margin-bottom:1.25rem">
        <img src="../assets/logo.png" alt="" width="42" height="42" />
        <div>
          <h1>Admin login</h1>
          <p class="sub" style="margin:0">Leads CRM — Bharatweld / Shubhshrey</p>
        </div>
      </div>

      <?php if ($error !== ''): ?>
        <p class="msg msg--err"><?= shubh_h($error) ?></p>
      <?php endif; ?>

      <form method="post" autocomplete="username">
        <?= shubh_csrf_field() ?>
        <div class="field">
          <label for="email">Email</label>
          <input id="email" name="email" type="email" required autocomplete="username" value="<?= shubh_h($_POST['email'] ?? '') ?>" />
        </div>
        <div class="field">
          <label for="password">Password</label>
          <input id="password" name="password" type="password" required autocomplete="current-password" />
        </div>
        <button class="btn btn--primary" type="submit">Sign in</button>
      </form>
    </div>
  </div>
</body>
</html>
