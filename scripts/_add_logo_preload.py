from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = '  <link rel="preload" href="assets/logo.png" as="image" />\n'
NEEDLE = '<link rel="icon" href="assets/logo.png" type="image/png" />'

for path in sorted(ROOT.glob("*.html")):
    text = path.read_text(encoding="utf-8")
    if 'id="site-preloader"' not in text:
        continue
    if 'href="assets/logo.png" as="image"' in text:
        continue
    if NEEDLE not in text:
        continue
    text = text.replace(NEEDLE, NEEDLE + "\n" + LINK, 1)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"preload {path.name}")
