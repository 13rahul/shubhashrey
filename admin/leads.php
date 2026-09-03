<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/includes/bootstrap.php';
shubh_require_admin();

$config = shubh_config();
$msg = '';
$error = '';
$statuses = shubh_lead_statuses();
$sources = shubh_lead_sources();
require_once __DIR__ . '/_lead_fields.php';
require_once dirname(__DIR__) . '/includes/geo_data.php';

function shubh_redirect_leads(array $extra = []): void
{
    $params = [
        'q' => $_GET['q'] ?? null,
        'status' => $_GET['status'] ?? null,
        'label' => $_GET['label'] ?? null,
        'source' => $_GET['source'] ?? null,
        'state' => $_GET['state'] ?? null,
        'district' => $_GET['district'] ?? null,
        'midc' => $_GET['midc'] ?? null,
    ];
    if (array_key_exists('edit', $extra)) {
        $params['edit'] = $extra['edit'];
    } elseif (isset($_GET['edit'])) {
        $params['edit'] = $_GET['edit'];
    }
    if (!empty($extra['msg'])) {
        $params['msg'] = $extra['msg'];
    }
    $q = array_filter($params, static fn($v) => $v !== null && $v !== '' && $v !== 'all');
    header('Location: leads.php' . ($q ? ('?' . http_build_query($q)) : ''));
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        shubh_csrf_verify($_POST['csrf_token'] ?? null);
        $action = (string) ($_POST['action'] ?? '');

        if ($action === 'add_lead') {
            $name = trim((string) ($_POST['name'] ?? ''));
            if ($name === '') {
                throw new RuntimeException('Name is required to add a lead.');
            }
            $id = shubh_lead_create($_POST);
            shubh_redirect_leads(['msg' => 'added', 'edit' => (string) $id]);
        }

        if ($action === 'save_lead') {
            $id = (int) ($_POST['id'] ?? 0);
            if ($id <= 0) {
                throw new RuntimeException('Invalid lead.');
            }
            if (trim((string) ($_POST['name'] ?? '')) === '') {
                throw new RuntimeException('Name is required.');
            }
            shubh_lead_update($id, $_POST);
            shubh_redirect_leads(['msg' => 'saved', 'edit' => (string) $id]);
        }

        if ($action === 'add_note') {
            $id = (int) ($_POST['id'] ?? 0);
            $note = trim((string) ($_POST['note'] ?? ''));
            if ($id <= 0 || $note === '') {
                throw new RuntimeException('Enter a note for the selected lead.');
            }
            shubh_lead_append_note($id, $note);
            shubh_redirect_leads(['msg' => 'note', 'edit' => (string) $id]);
        }

        if ($action === 'delete') {
            $id = (int) ($_POST['id'] ?? 0);
            if ($id > 0) {
                $stmt = shubh_db()->prepare('DELETE FROM leads WHERE id = :id');
                $stmt->execute([':id' => $id]);
            }
            shubh_redirect_leads(['msg' => 'deleted']);
        }

        if ($action === 'change_password') {
            $pass = (string) ($_POST['new_password'] ?? '');
            $pass2 = (string) ($_POST['new_password2'] ?? '');
            if ($pass !== $pass2) {
                throw new RuntimeException('Passwords do not match.');
            }
            if (!shubh_update_admin_password($pass)) {
                throw new RuntimeException('Password must be at least 8 characters.');
            }
            shubh_redirect_leads(['msg' => 'password']);
        }
    } catch (Throwable $e) {
        $error = $e->getMessage();
    }
}

$q = trim((string) ($_GET['q'] ?? ''));
$statusFilter = (string) ($_GET['status'] ?? 'all');
$labelFilter = (string) ($_GET['label'] ?? 'all');
$sourceFilter = (string) ($_GET['source'] ?? 'all');
$stateFilter = (string) ($_GET['state'] ?? 'all');
$districtFilter = (string) ($_GET['district'] ?? 'all');
$midcFilter = (string) ($_GET['midc'] ?? 'all');
$editId = (int) ($_GET['edit'] ?? 0);

if (isset($_GET['msg'])) {
    $map = [
        'added' => 'Lead added.',
        'saved' => 'Lead saved.',
        'note' => 'Note added.',
        'deleted' => 'Lead deleted.',
        'password' => 'Admin password updated.',
    ];
    $msg = $map[$_GET['msg']] ?? '';
}

$all = shubh_db()->query('SELECT * FROM leads ORDER BY datetime(created_at) DESC, id DESC')->fetchAll();

$counts = [
    'total' => count($all),
    'new' => 0,
    'contacted' => 0,
    'qualified' => 0,
    'won' => 0,
    'lost' => 0,
    'inbound' => 0,
    'prospect' => 0,
];
foreach ($all as $row) {
    $s = $row['status'] ?? 'new';
    if (isset($counts[$s])) {
        $counts[$s]++;
    }
    $lb = $row['lead_label'] ?? '';
    if ($lb === 'Inbound') {
        $counts['inbound']++;
    } elseif ($lb === 'Prospect') {
        $counts['prospect']++;
    }
}

$leads = $all;
if ($statusFilter !== 'all') {
    $leads = array_values(array_filter($leads, static fn($l) => ($l['status'] ?? '') === $statusFilter));
}
if ($labelFilter !== 'all') {
    $leads = array_values(array_filter($leads, static fn($l) => ($l['lead_label'] ?? '') === $labelFilter));
}
if ($sourceFilter !== 'all') {
    $leads = array_values(array_filter($leads, static fn($l) => ($l['source'] ?? '') === $sourceFilter));
}
if ($stateFilter !== 'all') {
    $leads = array_values(array_filter($leads, static fn($l) => ($l['state'] ?? '') === $stateFilter));
}
if ($districtFilter !== 'all') {
    $leads = array_values(array_filter($leads, static fn($l) => ($l['district'] ?? '') === $districtFilter));
}
if ($midcFilter !== 'all') {
    $leads = array_values(array_filter($leads, static fn($l) => ($l['midc'] ?? '') === $midcFilter));
}
if ($q !== '') {
    $needle = mb_strtolower($q);
    $leads = array_values(array_filter($leads, static function ($l) use ($needle) {
        $hay = mb_strtolower(implode(' ', [
            $l['name'], $l['email'], $l['phone'], $l['company'], $l['city'],
            $l['district'], $l['state'], $l['midc'], $l['territory'], $l['message'], $l['notes'], $l['interest'],
            $l['lead_label'] ?? '', $l['source'] ?? '',
        ]));
        return str_contains($hay, $needle);
    }));
}

$stateOptions = array_values(array_unique(array_merge(
    shubh_state_suggestions(),
    shubh_distinct_lead_values('state')
)));
sort($stateOptions, SORT_NATURAL | SORT_FLAG_CASE);

$districtOptions = array_values(array_unique(array_merge(
    shubh_district_suggestions($stateFilter !== 'all' ? $stateFilter : null),
    shubh_distinct_lead_values('district')
)));
sort($districtOptions, SORT_NATURAL | SORT_FLAG_CASE);

$midcOptions = array_values(array_unique(array_merge(
    shubh_midcs_for(
        $stateFilter !== 'all' ? $stateFilter : '',
        $districtFilter !== 'all' ? $districtFilter : ''
    ),
    // When browsing all locations, still allow filtering by any known MIDC
    ($stateFilter === 'all' && $districtFilter === 'all')
        ? array_merge(shubh_midc_suggestions(), shubh_distinct_lead_values('midc'))
        : shubh_distinct_lead_values('midc')
)));
sort($midcOptions, SORT_NATURAL | SORT_FLAG_CASE);

$districtsByState = shubh_state_districts_map();
$districtsByStateJson = json_encode($districtsByState, JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP);
$midcsByStateDistrict = shubh_midcs_by_state_district();
$midcsByStateDistrictJson = json_encode($midcsByStateDistrict, JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP);
$midcFallbackJson = json_encode(shubh_midc_fallback_options(), JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP);

$editing = null;
if ($editId > 0) {
    foreach ($all as $row) {
        if ((int) $row['id'] === $editId) {
            $editing = $row;
            break;
        }
    }
}

$csvRows = [['ID', 'Label', 'Status', 'Source', 'Name', 'Company', 'Phone', 'Email', 'City', 'District', 'State', 'MIDC', 'Territory', 'Business type', 'Interest', 'Message', 'Notes', 'Created']];
foreach ($leads as $l) {
    $csvRows[] = [
        $l['id'], $l['lead_label'] ?? '', $l['status'], $l['source'], $l['name'], $l['company'], $l['phone'], $l['email'],
        $l['city'], $l['district'], $l['state'], $l['midc'], $l['territory'], $l['business_type'],
        $l['interest'], str_replace(["\r", "\n"], ' ', (string) $l['message']),
        str_replace(["\r", "\n"], ' ', (string) $l['notes']), $l['created_at'],
    ];
}
$csv = '';
foreach ($csvRows as $row) {
    $csv .= implode(',', array_map(static fn($c) => '"' . str_replace('"', '""', (string) $c) . '"', $row)) . "\n";
}

function shubh_filter_qs(array $overrides = []): string
{
    $base = [
        'q' => $_GET['q'] ?? '',
        'status' => $_GET['status'] ?? 'all',
        'label' => $_GET['label'] ?? 'all',
        'source' => $_GET['source'] ?? 'all',
        'state' => $_GET['state'] ?? 'all',
        'district' => $_GET['district'] ?? 'all',
        'midc' => $_GET['midc'] ?? 'all',
        'edit' => $_GET['edit'] ?? '',
    ];
    $merged = array_merge($base, $overrides);
    $clean = [];
    foreach ($merged as $k => $v) {
        if ($v === null || $v === '' || $v === 'all') {
            continue;
        }
        $clean[$k] = $v;
    }
    return $clean ? ('?' . http_build_query($clean)) : '';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex,nofollow" />
  <title>Leads CRM | <?= shubh_h($config['site_name'] ?? 'Shubhshrey') ?></title>
  <link rel="icon" href="../assets/logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/admin.css" />
  <link rel="stylesheet" href="assets/crm-table.css" />
</head>
<body>
  <div class="admin-shell admin-shell--wide">
    <div class="admin-top">
      <div class="admin-brand">
        <img src="../assets/logo.png" alt="" width="42" height="42" />
        <div>
          <h1>Leads CRM</h1>
          <p>Inbound website forms + Bhosari prospects — filter by Lead label</p>
        </div>
      </div>
      <div class="admin-nav">
        <button class="btn btn--primary btn--sm" type="button" data-open-panel="add">+ Add lead</button>
        <?php if (count($leads) > 0): ?>
          <a class="btn btn--ghost btn--sm" href="data:text/csv;charset=utf-8,<?= rawurlencode($csv) ?>" download="shubhshrey-leads-<?= date('Y-m-d') ?>.csv">Export Excel/CSV</a>
        <?php endif; ?>
        <a class="btn btn--ghost btn--sm" href="../index.html" target="_blank" rel="noopener">View site</a>
        <a class="btn btn--ghost btn--sm" href="logout.php">Log out</a>
      </div>
    </div>

    <?php if ($msg !== ''): ?><p class="msg msg--ok"><?= shubh_h($msg) ?></p><?php endif; ?>
    <?php if ($error !== ''): ?><p class="msg msg--err"><?= shubh_h($error) ?></p><?php endif; ?>

    <div class="stats">
      <div class="stat"><strong><?= (int) $counts['total'] ?></strong><span>Total</span></div>
      <div class="stat"><strong><?= (int) $counts['inbound'] ?></strong><span>Inbound</span></div>
      <div class="stat"><strong><?= (int) $counts['prospect'] ?></strong><span>Prospect</span></div>
      <div class="stat"><strong><?= (int) $counts['new'] ?></strong><span>New</span></div>
      <div class="stat"><strong><?= (int) $counts['contacted'] ?></strong><span>Contacted</span></div>
      <div class="stat"><strong><?= (int) $counts['qualified'] ?></strong><span>Qualified</span></div>
      <div class="stat"><strong><?= count($leads) ?></strong><span>Showing</span></div>
    </div>

    <form class="filter-bar card card-pad" method="get" action="leads.php">
      <div class="field">
        <label for="q">Search</label>
        <input id="q" name="q" type="search" value="<?= shubh_h($q) ?>" placeholder="Name, phone, company, MIDC…" />
      </div>
      <div class="field">
        <label for="status">Status</label>
        <select id="status" name="status">
          <option value="all">All</option>
          <?php foreach ($statuses as $st): ?>
            <option value="<?= shubh_h($st) ?>" <?= $statusFilter === $st ? 'selected' : '' ?>><?= shubh_h(ucfirst($st)) ?></option>
          <?php endforeach; ?>
        </select>
      </div>
      <div class="field">
        <label for="label">Lead label</label>
        <select id="label" name="label">
          <option value="all">All labels</option>
          <?php foreach (shubh_lead_labels() as $lb): ?>
            <option value="<?= shubh_h($lb) ?>" <?= $labelFilter === $lb ? 'selected' : '' ?>><?= shubh_h($lb) ?></option>
          <?php endforeach; ?>
        </select>
      </div>
      <div class="field">
        <label for="source">Source</label>
        <select id="source" name="source">
          <option value="all">All</option>
          <?php foreach ($sources as $src): ?>
            <option value="<?= shubh_h($src) ?>" <?= $sourceFilter === $src ? 'selected' : '' ?>><?= shubh_h($src) ?></option>
          <?php endforeach; ?>
        </select>
      </div>
      <div class="field">
        <label for="state">State</label>
        <select id="state" name="state">
          <option value="all">All states</option>
          <?php foreach ($stateOptions as $st): ?>
            <option value="<?= shubh_h($st) ?>" <?= $stateFilter === $st ? 'selected' : '' ?>><?= shubh_h($st) ?></option>
          <?php endforeach; ?>
        </select>
      </div>
      <div class="field">
        <label for="district">District</label>
        <select id="district" name="district">
          <option value="all">All districts</option>
          <?php foreach ($districtOptions as $d): ?>
            <option value="<?= shubh_h($d) ?>" <?= $districtFilter === $d ? 'selected' : '' ?>><?= shubh_h($d) ?></option>
          <?php endforeach; ?>
        </select>
      </div>
      <div class="field">
        <label for="midc">MIDC</label>
        <select id="midc" name="midc">
          <option value="all">All MIDC</option>
          <?php foreach ($midcOptions as $m): ?>
            <option value="<?= shubh_h($m) ?>" <?= $midcFilter === $m ? 'selected' : '' ?>><?= shubh_h($m) ?></option>
          <?php endforeach; ?>
        </select>
      </div>
      <div class="filter-actions">
        <button class="btn btn--primary btn--sm" type="submit">Apply filters</button>
        <a class="btn btn--ghost btn--sm" href="leads.php">Clear</a>
      </div>
    </form>

    <div class="sheet-wrap card">
      <div class="table-wrap sheet-scroll">
        <table class="sheet">
          <thead>
            <tr>
              <th>ID</th>
              <th>Label</th>
              <th>Status</th>
              <th>Source</th>
              <th>Name</th>
              <th>Company</th>
              <th>Phone</th>
              <th>Email</th>
              <th>City</th>
              <th>District</th>
              <th>State</th>
              <th>MIDC</th>
              <th>Territory</th>
              <th>Interest</th>
              <th>Notes</th>
              <th>Created</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <?php if (!$leads): ?>
              <tr><td colspan="17" class="empty">No leads match. Click <strong>+ Add lead</strong> or clear filters.</td></tr>
            <?php else: ?>
              <?php foreach ($leads as $lead):
                  $isEdit = $editId === (int) $lead['id'];
                  $created = $lead['created_at'] ? date('Y-m-d H:i', strtotime((string) $lead['created_at'])) : '';
                  $label = (string) ($lead['lead_label'] ?? '');
                  $labelClass = strtolower($label !== '' ? $label : 'manual');
              ?>
                <tr class="<?= $isEdit ? 'is-selected' : '' ?>" id="row-<?= (int) $lead['id'] ?>">
                  <td><?= (int) $lead['id'] ?></td>
                  <td><span class="badge badge-label-<?= shubh_h($labelClass) ?>"><?= shubh_h($label !== '' ? $label : '—') ?></span></td>
                  <td><span class="badge badge-<?= shubh_h($lead['status'] ?: 'new') ?>"><?= shubh_h($lead['status'] ?: 'new') ?></span></td>
                  <td><?= shubh_h($lead['source']) ?></td>
                  <td><?= shubh_h($lead['name']) ?></td>
                  <td><?= shubh_h($lead['company']) ?></td>
                  <td><?= shubh_h($lead['phone']) ?></td>
                  <td><?= shubh_h($lead['email']) ?></td>
                  <td><?= shubh_h($lead['city']) ?></td>
                  <td><?= shubh_h($lead['district']) ?></td>
                  <td><?= shubh_h($lead['state']) ?></td>
                  <td><?= shubh_h($lead['midc']) ?></td>
                  <td><?= shubh_h($lead['territory']) ?></td>
                  <td><?= shubh_h($lead['interest']) ?></td>
                  <td class="notes-cell" title="<?= shubh_h($lead['notes']) ?>"><?= shubh_h(mb_strimwidth((string) $lead['notes'], 0, 48, '…')) ?></td>
                  <td class="muted"><?= shubh_h($created) ?></td>
                  <td class="actions-cell">
                    <a class="btn btn--ghost btn--sm" href="leads.php<?= shubh_h(shubh_filter_qs(['edit' => (string) $lead['id']])) ?>#editor">Edit</a>
                    <button class="btn btn--ghost btn--sm" type="button" data-note-for="<?= (int) $lead['id'] ?>" data-note-name="<?= shubh_h($lead['name']) ?>">+ Note</button>
                  </td>
                </tr>
              <?php endforeach; ?>
            <?php endif; ?>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Add lead panel -->
    <div class="panel card card-pad" id="panel-add" hidden>
      <div class="panel-head">
        <h2>Add lead</h2>
        <button class="btn btn--ghost btn--sm" type="button" data-close-panel="add">Close</button>
      </div>
      <form method="post" class="form-grid-crm">
        <?= shubh_csrf_field() ?>
        <input type="hidden" name="action" value="add_lead" />
        <?php
        $blank = array_fill_keys(shubh_lead_field_keys(), '');
        $blank['source'] = 'manual';
        $blank['lead_label'] = 'Manual';
        $blank['status'] = 'new';
        $blank['state'] = 'Maharashtra';
        render_lead_fields($blank, $statuses, $sources, $stateOptions, $midcOptions, 'add', $districtsByState);
        ?>
        <div class="form-actions">
          <button class="btn btn--primary" type="submit">Save new lead</button>
        </div>
      </form>
    </div>

    <!-- Edit lead panel -->
    <div class="panel card card-pad" id="editor" <?= $editing ? '' : 'hidden' ?>>
      <?php if ($editing): ?>
        <div class="panel-head">
          <h2>Edit lead #<?= (int) $editing['id'] ?> — <?= shubh_h($editing['name']) ?></h2>
          <a class="btn btn--ghost btn--sm" href="leads.php<?= shubh_h(shubh_filter_qs(['edit' => null])) ?>">Close</a>
        </div>
        <form method="post" class="form-grid-crm">
          <?= shubh_csrf_field() ?>
          <input type="hidden" name="action" value="save_lead" />
          <input type="hidden" name="id" value="<?= (int) $editing['id'] ?>" />
          <?php
          render_lead_fields($editing, $statuses, $sources, $stateOptions, $midcOptions, 'edit', $districtsByState);
          ?>
          <div class="form-actions">
            <button class="btn btn--primary" type="submit">Save all fields</button>
          </div>
        </form>
        <form method="post" class="note-form" style="margin-top:1rem">
          <?= shubh_csrf_field() ?>
          <input type="hidden" name="action" value="add_note" />
          <input type="hidden" name="id" value="<?= (int) $editing['id'] ?>" />
          <div class="field">
            <label for="note_append">Add note</label>
            <textarea id="note_append" name="note" rows="2" placeholder="Call outcome, next follow-up…" required></textarea>
          </div>
          <button class="btn btn--ghost btn--sm" type="submit" style="margin-top:.5rem">Append note</button>
        </form>
        <form method="post" style="margin-top:1rem" onsubmit="return confirm('Delete this lead permanently?');">
          <?= shubh_csrf_field() ?>
          <input type="hidden" name="action" value="delete" />
          <input type="hidden" name="id" value="<?= (int) $editing['id'] ?>" />
          <button class="btn btn--danger btn--sm" type="submit">Delete lead</button>
        </form>
      <?php else: ?>
        <p class="muted" style="margin:0">Select <strong>Edit</strong> on a row to change every field.</p>
      <?php endif; ?>
    </div>

    <!-- Quick add-note modal -->
    <div class="modal" id="note-modal" hidden>
      <div class="modal-card card card-pad">
        <div class="panel-head">
          <h2 id="note-modal-title">Add note</h2>
          <button class="btn btn--ghost btn--sm" type="button" data-close-note>Close</button>
        </div>
        <form method="post">
          <?= shubh_csrf_field() ?>
          <input type="hidden" name="action" value="add_note" />
          <input type="hidden" name="id" id="note-lead-id" value="" />
          <div class="field">
            <label for="note_modal_text">Note</label>
            <textarea id="note_modal_text" name="note" rows="4" required placeholder="Call outcome, next follow-up…"></textarea>
          </div>
          <button class="btn btn--primary" type="submit" style="margin-top:.75rem">Save note</button>
        </form>
      </div>
    </div>

    <div class="card card-pad" style="margin-top:1.5rem">
      <h2 style="margin:0 0 .75rem;font-family:var(--font-display);font-size:1.05rem">Change admin password</h2>
      <form method="post" class="filters">
        <?= shubh_csrf_field() ?>
        <input type="hidden" name="action" value="change_password" />
        <div class="field">
          <label for="new_password">New password</label>
          <input id="new_password" type="password" name="new_password" minlength="8" required autocomplete="new-password" />
        </div>
        <div class="field">
          <label for="new_password2">Confirm</label>
          <input id="new_password2" type="password" name="new_password2" minlength="8" required autocomplete="new-password" />
        </div>
        <button class="btn btn--primary btn--sm" type="submit">Update password</button>
      </form>
      <p class="muted" style="margin:.75rem 0 0">Signed in as <?= shubh_h($_SESSION['admin_email'] ?? '') ?></p>
    </div>
  </div>

  <script>
    window.SHUBH_DISTRICTS_BY_STATE = <?= $districtsByStateJson ?: '{}' ?>;
    window.SHUBH_MIDCS_BY_STATE_DISTRICT = <?= $midcsByStateDistrictJson ?: '{}' ?>;
    window.SHUBH_MIDC_FALLBACK = <?= $midcFallbackJson ?: '[]' ?>;
  </script>
  <script src="assets/geo-cascade.js"></script>
  <script>
    (function () {
      const addPanel = document.getElementById('panel-add');
      const noteModal = document.getElementById('note-modal');
      document.querySelectorAll('[data-open-panel="add"]').forEach((btn) => {
        btn.addEventListener('click', () => {
          addPanel.hidden = false;
          addPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      });
      document.querySelectorAll('[data-close-panel="add"]').forEach((btn) => {
        btn.addEventListener('click', () => { addPanel.hidden = true; });
      });
      document.querySelectorAll('[data-note-for]').forEach((btn) => {
        btn.addEventListener('click', () => {
          document.getElementById('note-lead-id').value = btn.getAttribute('data-note-for');
          document.getElementById('note-modal-title').textContent =
            'Add note — ' + (btn.getAttribute('data-note-name') || 'Lead');
          noteModal.hidden = false;
          document.getElementById('note_modal_text').focus();
        });
      });
      document.querySelectorAll('[data-close-note]').forEach((btn) => {
        btn.addEventListener('click', () => { noteModal.hidden = true; });
      });
      if (noteModal) {
        noteModal.addEventListener('click', (e) => {
          if (e.target === noteModal) noteModal.hidden = true;
        });
      }
      <?php if ($editing): ?>
      document.getElementById('editor')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      <?php endif; ?>
    })();
  </script>
</body>
</html>
