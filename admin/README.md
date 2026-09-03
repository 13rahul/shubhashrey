# Shubhshrey Admin CRM

Lean leads admin inspired by College Discovery’s `/admin/leads` triage (filters, status, notes, WhatsApp, CSV) and Slayly’s PHP session login.

## URL

- Local (XAMPP): `http://localhost/Subhshrey-industries/admin/login.php`
- Production: `https://your-domain/admin/login.php`

## Default login (change immediately)

| Field | Value |
|-------|--------|
| Email | `admin@shubhshrey.com` |
| Password | `ChangeMe@2026` |

After login, use **Change admin password** at the bottom of the leads page.

## Features

- Excel-style leads table (sticky header, horizontal scroll)
- **+ Add lead** (manual entry)
- **Edit all fields** (name, company, phone, email, city, **district**, **state**, **MIDC**, territory, interest, message, status, source, notes)
- **+ Note** per lead (timestamped append)
- Filters: search, status, source, **state** (all India), **district** (cascading by state), **MIDC** (filtered by state/district)
- Geo master lists in `includes/geo_data.php` (36 MH districts, full India states/districts map, MIDC industrial areas)
- Import Bhosari prospect CSV into CRM: `php scripts/import_bhosari_to_crm.php --replace-tests`

## Default login (change immediately)

| Field | Value |
|-------|--------|
| Email | `admin@shubhshrey.com` |
| Password | `ChangeMe@2026` |

URL: `http://localhost/Subhshrey-industries/admin/login.php`

## Files

- `admin/` — login, leads list, lead detail, CSS
- `includes/` — bootstrap, auth, SQLite, CSRF
- `config/admin.php` — credentials (protected by `.htaccess`)
- `storage/crm.sqlite` — auto-created (gitignored)
- `api/lead.php` — public create-lead endpoint

## Security notes

- `config/`, `includes/`, and `storage/` deny direct web access via `.htaccess`
- Do not commit a production password; rotate after deploy
- Admin is not linked from the public nav
