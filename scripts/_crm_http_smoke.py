"""HTTP acceptance for admin login + lead API against local PHP server."""
from __future__ import annotations

import json
import re
import sqlite3
import sys
import urllib.error
import urllib.parse
import urllib.request
from http.cookiejar import CookieJar
from pathlib import Path

BASE = "http://127.0.0.1:8787"
ROOT = Path(__file__).resolve().parents[1]
failures = 0


def ok(msg: str) -> None:
    print(f"OK  {msg}")


def fail(msg: str) -> None:
    global failures
    failures += 1
    print(f"FAIL {msg}")


def request(opener, method: str, path: str, data: dict | None = None, json_body: dict | None = None):
    url = BASE + path
    headers = {}
    body = None
    if json_body is not None:
        body = json.dumps(json_body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    elif data is not None:
        body = urllib.parse.urlencode(data).encode("utf-8")
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with opener.open(req) as res:
            return res.getcode(), res.read().decode("utf-8", "replace"), dict(res.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace"), dict(e.headers)


def main() -> int:
    jar = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

    # Unauthenticated leads should redirect to login
    code, html, headers = request(opener, "GET", "/admin/leads.php")
    loc = headers.get("Location") or headers.get("location") or ""
    if code in (301, 302, 303, 307, 308) and "login.php" in loc:
        ok(f"unauth leads redirects ({code} -> {loc})")
    elif code == 200 and ("Admin login" in html or 'name="password"' in html):
        ok("unauth leads showed login")
    else:
        # PHP built-in may follow differently; check final content
        if 'name="password"' in html and "Admin login" in html:
            ok("unauth leads ended on login form")
        else:
            fail(f"unauth leads unexpected code={code} loc={loc}")

    # Fresh opener for login flow
    jar = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    code, login_html, _ = request(opener, "GET", "/admin/login.php")
    m = re.search(r'name="csrf_token" value="([^"]+)"', login_html)
    if not m:
        fail("csrf token missing on login page")
        return 1
    csrf = m.group(1)
    ok("login page csrf present")

    code, after, headers = request(
        opener,
        "POST",
        "/admin/login.php",
        data={
            "csrf_token": csrf,
            "email": "admin@shubhshrey.com",
            "password": "ChangeMe@2026",
        },
    )
    # May be 302 to leads, or 200 with leads content if followed
    code2, leads_html, _ = request(opener, "GET", "/admin/leads.php")
    if code2 == 200 and ("HTTP Smoke" in leads_html or "badge-new" in leads_html or "Add lead" in leads_html):
        ok("authenticated leads page loads")
    else:
        fail(f"leads page after login code={code2}")

    if "logout.php" in leads_html:
        ok("logout link present")
    else:
        fail("logout link missing")

    # API already created smoke leads earlier; create one more and confirm visible
    code, body, _ = request(
        opener,
        "POST",
        "/api/lead.php",
        json_body={
            "source": "contact",
            "name": "HTTP Smoke Visible",
            "email": "http.smoke.visible@example.com",
            "phone": "9555555555",
            "message": "visible in admin",
        },
    )
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        payload = {}
    if code == 200 and payload.get("success"):
        ok(f"api lead create id={payload.get('id')}")
    else:
        fail(f"api lead create failed code={code} body={body[:200]}")

    _, leads_html, _ = request(opener, "GET", "/admin/leads.php")
    if "HTTP Smoke Visible" in leads_html:
        ok("new inbound lead appears in admin list")
    else:
        fail("new inbound lead not visible in admin list")

    # Cleanup smoke emails
    db = ROOT / "storage" / "crm.sqlite"
    con = sqlite3.connect(str(db))
    n = con.execute("DELETE FROM leads WHERE email LIKE 'http.smoke.%'").rowcount
    con.commit()
    con.close()
    ok(f"cleaned {n} http smoke leads")

    print()
    if failures:
        print(f"{failures} FAILURE(S)")
        return 1
    print("ALL PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
