<?php
declare(strict_types=1);

function shubh_db(): PDO
{
    static $pdo;
    if ($pdo instanceof PDO) {
        return $pdo;
    }

    if (!is_dir(SHUBH_STORAGE)) {
        mkdir(SHUBH_STORAGE, 0755, true);
    }

    $dbPath = SHUBH_STORAGE . '/crm.sqlite';
    $pdo = new PDO('sqlite:' . $dbPath, null, null, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
    $pdo->exec('PRAGMA foreign_keys = ON');
    shubh_db_migrate($pdo);
    return $pdo;
}

function shubh_db_migrate(PDO $pdo): void
{
    $pdo->exec(
        'CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL DEFAULT \'contact\',
            name TEXT NOT NULL DEFAULT \'\',
            email TEXT NOT NULL DEFAULT \'\',
            phone TEXT NOT NULL DEFAULT \'\',
            company TEXT NOT NULL DEFAULT \'\',
            city TEXT NOT NULL DEFAULT \'\',
            district TEXT NOT NULL DEFAULT \'\',
            state TEXT NOT NULL DEFAULT \'\',
            midc TEXT NOT NULL DEFAULT \'\',
            territory TEXT NOT NULL DEFAULT \'\',
            business_type TEXT NOT NULL DEFAULT \'\',
            interest TEXT NOT NULL DEFAULT \'\',
            message TEXT NOT NULL DEFAULT \'\',
            status TEXT NOT NULL DEFAULT \'new\',
            notes TEXT NOT NULL DEFAULT \'\',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )'
    );

    // Upgrade older DBs missing columns
    $cols = [];
    foreach ($pdo->query('PRAGMA table_info(leads)') as $row) {
        $cols[$row['name']] = true;
    }
    if (!isset($cols['district'])) {
        $pdo->exec("ALTER TABLE leads ADD COLUMN district TEXT NOT NULL DEFAULT ''");
    }
    if (!isset($cols['midc'])) {
        $pdo->exec("ALTER TABLE leads ADD COLUMN midc TEXT NOT NULL DEFAULT ''");
    }

    $pdo->exec('CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS idx_leads_source ON leads(source)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS idx_leads_created ON leads(created_at)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS idx_leads_state ON leads(state)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS idx_leads_district ON leads(district)');
    $pdo->exec('CREATE INDEX IF NOT EXISTS idx_leads_midc ON leads(midc)');
}

/**
 * @return list<string>
 */
function shubh_lead_field_keys(): array
{
    return [
        'source', 'name', 'email', 'phone', 'company', 'city', 'district', 'state',
        'midc', 'territory', 'business_type', 'interest', 'message', 'status', 'notes',
    ];
}

/**
 * @param array<string, mixed> $data
 * @return array<string, string>
 */
function shubh_lead_normalize(array $data): array
{
    $out = [];
    foreach (shubh_lead_field_keys() as $key) {
        $out[$key] = trim((string) ($data[$key] ?? ''));
    }
    if ($out['source'] === '') {
        $out['source'] = 'manual';
    }
    if ($out['status'] === '' || !in_array($out['status'], shubh_lead_statuses(), true)) {
        $out['status'] = 'new';
    }
    return $out;
}

/**
 * @param array<string, mixed> $data
 */
function shubh_lead_create(array $data): int
{
    $row = shubh_lead_normalize($data);
    $now = date('c');
    $stmt = shubh_db()->prepare(
        'INSERT INTO leads (
            source, name, email, phone, company, city, district, state, midc, territory,
            business_type, interest, message, status, notes, created_at, updated_at
        ) VALUES (
            :source, :name, :email, :phone, :company, :city, :district, :state, :midc, :territory,
            :business_type, :interest, :message, :status, :notes, :created_at, :updated_at
        )'
    );
    $stmt->execute([
        ':source' => $row['source'],
        ':name' => $row['name'],
        ':email' => $row['email'],
        ':phone' => $row['phone'],
        ':company' => $row['company'],
        ':city' => $row['city'],
        ':district' => $row['district'],
        ':state' => $row['state'],
        ':midc' => $row['midc'],
        ':territory' => $row['territory'],
        ':business_type' => $row['business_type'],
        ':interest' => $row['interest'],
        ':message' => $row['message'],
        ':status' => $row['status'],
        ':notes' => $row['notes'],
        ':created_at' => $now,
        ':updated_at' => $now,
    ]);
    return (int) shubh_db()->lastInsertId();
}

/**
 * @param array<string, mixed> $data
 */
function shubh_lead_update(int $id, array $data): void
{
    if ($id <= 0) {
        throw new InvalidArgumentException('Invalid lead id.');
    }
    $row = shubh_lead_normalize($data);
    $stmt = shubh_db()->prepare(
        'UPDATE leads SET
            source = :source,
            name = :name,
            email = :email,
            phone = :phone,
            company = :company,
            city = :city,
            district = :district,
            state = :state,
            midc = :midc,
            territory = :territory,
            business_type = :business_type,
            interest = :interest,
            message = :message,
            status = :status,
            notes = :notes,
            updated_at = :updated_at
         WHERE id = :id'
    );
    $stmt->execute([
        ':source' => $row['source'],
        ':name' => $row['name'],
        ':email' => $row['email'],
        ':phone' => $row['phone'],
        ':company' => $row['company'],
        ':city' => $row['city'],
        ':district' => $row['district'],
        ':state' => $row['state'],
        ':midc' => $row['midc'],
        ':territory' => $row['territory'],
        ':business_type' => $row['business_type'],
        ':interest' => $row['interest'],
        ':message' => $row['message'],
        ':status' => $row['status'],
        ':notes' => $row['notes'],
        ':updated_at' => date('c'),
        ':id' => $id,
    ]);
}

function shubh_lead_append_note(int $id, string $note): void
{
    $note = trim($note);
    if ($id <= 0 || $note === '') {
        return;
    }
    $stmt = shubh_db()->prepare('SELECT notes FROM leads WHERE id = :id');
    $stmt->execute([':id' => $id]);
    $existing = (string) ($stmt->fetchColumn() ?: '');
    $stamp = date('Y-m-d H:i');
    $combined = trim($existing === '' ? "[{$stamp}] {$note}" : $existing . "\n[{$stamp}] {$note}");
    $upd = shubh_db()->prepare('UPDATE leads SET notes = :notes, updated_at = :u WHERE id = :id');
    $upd->execute([':notes' => $combined, ':u' => date('c'), ':id' => $id]);
}

/**
 * @return list<string>
 */
function shubh_lead_statuses(): array
{
    return ['new', 'contacted', 'qualified', 'won', 'lost'];
}

/**
 * @return list<string>
 */
function shubh_lead_sources(): array
{
    return ['contact', 'distributor', 'manual', 'visit', 'referral', 'phone', 'whatsapp'];
}

/**
 * @return list<string>
 */
function shubh_midc_suggestions(): array
{
    require_once __DIR__ . '/geo_data.php';
    return shubh_maharashtra_midc_list();
}

/**
 * @return list<string>
 */
function shubh_state_suggestions(): array
{
    require_once __DIR__ . '/geo_data.php';
    return shubh_india_states();
}

/**
 * @return list<string>
 */
function shubh_district_suggestions(?string $state = null): array
{
    require_once __DIR__ . '/geo_data.php';
    if ($state !== null && $state !== '' && $state !== 'all') {
        return shubh_districts_for_state($state);
    }
    return shubh_all_districts_flat();
}

/**
 * @return list<string>
 */
function shubh_distinct_lead_values(string $column): array
{
    $allowed = ['state', 'district', 'midc', 'source', 'status', 'city'];
    if (!in_array($column, $allowed, true)) {
        return [];
    }
    $stmt = shubh_db()->query(
        "SELECT DISTINCT {$column} AS v FROM leads WHERE TRIM({$column}) != '' ORDER BY v COLLATE NOCASE ASC"
    );
    $vals = [];
    foreach ($stmt as $row) {
        $vals[] = (string) $row['v'];
    }
    return $vals;
}
