"""Offline CRM acceptance checks (no PHP required for schema/files)."""
from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def ok(msg: str) -> None:
    print(f"OK  {msg}")


def fail(msg: str) -> None:
    errors.append(msg)
    print(f"FAIL {msg}")


def require_files() -> None:
    needed = [
        "admin/login.php",
        "admin/logout.php",
        "admin/index.php",
        "admin/leads.php",
        "admin/lead.php",
        "admin/assets/admin.css",
        "admin/README.md",
        "api/lead.php",
        "api/contact.php",
        "includes/bootstrap.php",
        "includes/auth.php",
        "includes/db.php",
        "includes/csrf.php",
        "config/admin.php",
        "config/.htaccess",
        "includes/.htaccess",
        "storage/.htaccess",
        "js/main.js",
    ]
    for rel in needed:
        path = ROOT / rel
        if path.is_file():
            ok(f"exists {rel}")
        else:
            fail(f"missing {rel}")


def check_htaccess() -> None:
    for rel in ("config/.htaccess", "includes/.htaccess", "storage/.htaccess"):
        text = (ROOT / rel).read_text(encoding="utf-8", errors="replace").lower()
        if "deny" in text or "require all denied" in text:
            ok(f"hardened {rel}")
        else:
            fail(f"{rel} does not deny web access")


def check_config() -> None:
    text = (ROOT / "config/admin.php").read_text(encoding="utf-8", errors="replace")
    if "admin@shubhshrey.com" in text:
        ok("admin email configured")
    else:
        fail("admin email missing")
    if "admin_password_hash" in text and "$2y$" in text:
        ok("password hash present")
    else:
        fail("password hash missing")
    readme = (ROOT / "admin/README.md").read_text(encoding="utf-8", errors="replace")
    if "ChangeMe@2026" in readme and "admin@shubhshrey.com" in readme:
        ok("README documents default credentials")
    else:
        fail("README missing default credentials")


def check_js_wiring() -> None:
    js = (ROOT / "js/main.js").read_text(encoding="utf-8", errors="replace")
    for needle in (
        "async function saveLead",
        'source: "contact"',
        'source: "distributor"',
        "api/lead.php",
        "Saved - WhatsApp opened",
    ):
        if needle in js:
            ok(f"main.js has {needle!r}")
        else:
            fail(f"main.js missing {needle!r}")


def check_admin_features() -> None:
    leads = (ROOT / "admin/leads.php").read_text(encoding="utf-8", errors="replace")
    for needle in (
        "shubh_require_admin",
        "add_lead",
        "save_lead",
        "add_note",
        "delete",
        "change_password",
        "status",
        "source",
    ):
        if needle in leads:
            ok(f"leads.php has {needle}")
        else:
            fail(f"leads.php missing {needle}")

    detail = (ROOT / "admin/lead.php").read_text(encoding="utf-8", errors="replace")
    for needle in ("shubh_require_admin", "add_note", "delete", "save"):
        if needle in detail:
            ok(f"lead.php has {needle}")
        else:
            fail(f"lead.php missing {needle}")

    login = (ROOT / "admin/login.php").read_text(encoding="utf-8", errors="replace")
    if "shubh_attempt_login" in login and "shubh_csrf" in login:
        ok("login.php uses auth + CSRF")
    else:
        fail("login.php auth/CSRF incomplete")


def check_sqlite() -> None:
    db_path = ROOT / "storage/crm.sqlite"
    if not db_path.is_file():
        fail("storage/crm.sqlite missing")
        return

    con = sqlite3.connect(str(db_path))
    cols = {row[1] for row in con.execute("PRAGMA table_info(leads)")}
    required = {
        "id",
        "source",
        "name",
        "email",
        "phone",
        "company",
        "city",
        "state",
        "territory",
        "business_type",
        "interest",
        "message",
        "status",
        "notes",
        "created_at",
        "updated_at",
    }
    missing = sorted(required - cols)
    if missing:
        fail(f"leads columns missing: {missing}")
    else:
        ok(f"leads schema has required columns ({len(cols)} total)")

    # Simulate API inserts for contact + distributor
    now = "2026-11-02T18:30:00+05:30"
    cur = con.cursor()
    cur.execute(
        """
        INSERT INTO leads (
            source, lead_label, name, email, phone, company, city, district, state, midc,
            territory, business_type, interest, message, status, notes, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "contact",
            "Inbound",
            "Smoke Contact",
            "smoke.contact@example.com",
            "9000000001",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "Smoke contact message",
            "new",
            "Inbound lead - Contact Us form | smoke",
            now,
            now,
        ),
    )
    contact_id = cur.lastrowid
    cur.execute(
        """
        INSERT INTO leads (
            source, lead_label, name, email, phone, company, city, district, state, midc,
            territory, business_type, interest, message, status, notes, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "distributor",
            "Inbound",
            "Smoke Dist",
            "smoke.dist@example.com",
            "9000000002",
            "Smoke Co",
            "Pune",
            "Pune",
            "Maharashtra",
            "",
            "Pune East",
            "Dealer",
            "E6013",
            "Want dealership",
            "new",
            "Inbound lead - Become a Distributor form | smoke",
            now,
            now,
        ),
    )
    dist_id = cur.lastrowid

    # Status update + note append
    cur.execute(
        "UPDATE leads SET status = ?, notes = notes || ?, updated_at = ? WHERE id = ?",
        ("contacted", "\n[smoke] called", now, contact_id),
    )
    row = cur.execute(
        "SELECT source, status, company, territory FROM leads WHERE id = ?",
        (dist_id,),
    ).fetchone()
    if row == ("distributor", "new", "Smoke Co", "Pune East"):
        ok(f"distributor lead fields ok id={dist_id}")
    else:
        fail(f"distributor lead unexpected: {row}")

    c_row = cur.execute("SELECT status FROM leads WHERE id = ?", (contact_id,)).fetchone()
    if c_row and c_row[0] == "contacted":
        ok(f"contact lead status update ok id={contact_id}")
    else:
        fail(f"contact status update failed: {c_row}")

    # Cleanup smoke rows
    cur.execute("DELETE FROM leads WHERE id IN (?, ?)", (contact_id, dist_id))
    con.commit()
    con.close()
    ok("cleaned smoke leads")


def check_api_source_gate() -> None:
    api = (ROOT / "api/lead.php").read_text(encoding="utf-8", errors="replace")
    if "contact" in api and "distributor" in api and "shubh_lead_create" in api:
        ok("api/lead.php creates contact/distributor leads")
    else:
        fail("api/lead.php incomplete")
    if re.search(r"lead_label['\"]?\s*=>\s*['\"]Inbound['\"]", api) or "'Inbound'" in api:
        ok("api/lead.php tags Inbound")
    else:
        fail("api/lead.php missing Inbound label")


def main() -> int:
    print(f"ROOT={ROOT}")
    require_files()
    check_htaccess()
    check_config()
    check_js_wiring()
    check_admin_features()
    check_api_source_gate()
    check_sqlite()
    print()
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=2))
        return 1
    print(json.dumps({"ok": True, "errors": []}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
