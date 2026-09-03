<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/includes/bootstrap.php';
shubh_require_admin();
require_once __DIR__ . '/_lead_fields.php';
require_once dirname(__DIR__) . '/includes/geo_data.php';

$config = shubh_config();
$id = (int) ($_GET['id'] ?? 0);
$error = '';
$msg = '';

if ($id <= 0) {
    header('Location: leads.php');
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        shubh_csrf_verify($_POST['csrf_token'] ?? null);
        $action = (string) ($_POST['action'] ?? '');

        if ($action === 'save') {
            if (trim((string) ($_POST['name'] ?? '')) === '') {
                throw new RuntimeException('Name is required.');
            }
            shubh_lead_update($id, $_POST);
            header('Location: lead.php?id=' . $id . '&msg=saved');
            exit;
        }

        if ($action === 'add_note') {
            shubh_lead_append_note($id, (string) ($_POST['note'] ?? ''));
            header('Location: lead.php?id=' . $id . '&msg=note');
            exit;
        }

        if ($action === 'delete') {
            $stmt = shubh_db()->prepare('DELETE FROM leads WHERE id = :id');
            $stmt->execute([':id' => $id]);
            header('Location: leads.php?msg=deleted');
            exit;
        }
    } catch (Throwable $e) {
        $error = $e->getMessage();
    }
}

$stmt = shubh_db()->prepare('SELECT * FROM leads WHERE id = :id');
$stmt->execute([':id' => $id]);
$lead = $stmt->fetch();
if (!$lead) {
    header('Location: leads.php');
    exit;
}

if (isset($_GET['msg'])) {
    $map = ['saved' => 'Lead updated.', 'note' => 'Note added.'];
    $msg = $map[$_GET['msg']] ?? '';
}

$stateOptions = array_values(array_unique(array_merge(
    shubh_state_suggestions(),
    shubh_distinct_lead_values('state')
)));
$midcOptions = array_values(array_unique(array_merge(
    shubh_midcs_for((string) ($lead['state'] ?? ''), (string) ($lead['district'] ?? '')),
    shubh_distinct_lead_values('midc')
)));
$districtsByState = shubh_state_districts_map();
$districtsByStateJson = json_encode($districtsByState, JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP);
$midcsByStateDistrictJson = json_encode(shubh_midcs_by_state_district(), JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP);
$midcFallbackJson = json_encode(shubh_midc_fallback_options(), JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP);
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex,nofollow" />
  <title>Lead #<?= (int) $lead['id'] ?> | Admin</title>
  <link rel="icon" href="../assets/logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/admin.css" />
  <link rel="stylesheet" href="assets/crm-table.css" />
</head>
<body>
  <div class="admin-shell">
    <div class="admin-top">
      <div class="admin-brand">
        <img src="../assets/logo.png" alt="" width="42" height="42" />
        <div>
          <h1><?= shubh_h($lead['name']) ?></h1>
          <p>Lead #<?= (int) $lead['id'] ?> · edit all fields</p>
        </div>
      </div>
      <div class="admin-nav">
        <a class="btn btn--ghost btn--sm" href="leads.php?edit=<?= (int) $lead['id'] ?>">Back to table</a>
        <a class="btn btn--ghost btn--sm" href="logout.php">Log out</a>
      </div>
    </div>

    <?php if ($msg !== ''): ?><p class="msg msg--ok"><?= shubh_h($msg) ?></p><?php endif; ?>
    <?php if ($error !== ''): ?><p class="msg msg--err"><?= shubh_h($error) ?></p><?php endif; ?>

    <div class="card card-pad">
      <form method="post" class="form-grid-crm">
        <?= shubh_csrf_field() ?>
        <input type="hidden" name="action" value="save" />
        <?php render_lead_fields($lead, shubh_lead_statuses(), shubh_lead_sources(), $stateOptions, $midcOptions, 'detail', $districtsByState); ?>
        <div class="form-actions">
          <button class="btn btn--primary" type="submit">Save all fields</button>
        </div>
      </form>
      <form method="post" style="margin-top:1rem">
        <?= shubh_csrf_field() ?>
        <input type="hidden" name="action" value="add_note" />
        <div class="field">
          <label for="note">Add note</label>
          <textarea id="note" name="note" rows="2" required></textarea>
        </div>
        <button class="btn btn--ghost btn--sm" type="submit" style="margin-top:.5rem">Append note</button>
      </form>
      <form method="post" style="margin-top:1rem" onsubmit="return confirm('Delete this lead permanently?');">
        <?= shubh_csrf_field() ?>
        <input type="hidden" name="action" value="delete" />
        <button class="btn btn--danger btn--sm" type="submit">Delete lead</button>
      </form>
    </div>
  </div>
  <script>
    window.SHUBH_DISTRICTS_BY_STATE = <?= $districtsByStateJson ?: '{}' ?>;
    window.SHUBH_MIDCS_BY_STATE_DISTRICT = <?= $midcsByStateDistrictJson ?: '{}' ?>;
    window.SHUBH_MIDC_FALLBACK = <?= $midcFallbackJson ?: '[]' ?>;
  </script>
  <script src="assets/geo-cascade.js"></script>
</body>
</html>
