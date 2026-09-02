# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(r"d:\New folder\htdocs\Subhshrey-industries")
FOOTER = (ROOT / "scripts" / "_footer_resources.html").read_text(encoding="utf-8")
FOOTER_RE = re.compile(r'<footer class="site-footer">.*?</footer>', re.DOTALL)
skip = {"vision.html", "mission.html"}

for path in ROOT.glob("*.html"):
    if path.name in skip:
        continue
    raw = path.read_bytes()
    text = None
    used = None
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc)
            used = enc
            break
        except UnicodeDecodeError:
            continue
    if text is None or "site-footer" not in text:
        print("SKIP", path.name)
        continue

    text = text.replace("Bharatweld \x97 Proudly", "Bharatweld — Proudly")
    text = text.replace("Bharatweld â Proudly", "Bharatweld — Proudly")
    new_text, n = FOOTER_RE.subn(FOOTER, text, count=1)
    if n:
        new_text = re.sub(
            r'href="css/styles\.css\?v=\d+"',
            'href="css/styles.css?v=14"',
            new_text,
        )
        path.write_text(new_text, encoding="utf-8")
        print("Updated", path.name, "(" + used + ")")
    else:
        print("No match", path.name)
