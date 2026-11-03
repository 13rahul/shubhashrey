from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OLD = 'src="assets/make-in-india-white.png"'
NEW = 'src="assets/make-in-india-white.png?v=2"'

for path in list(ROOT.glob("*.html")) + [ROOT / "scripts" / "_footer_resources.html"]:
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    if OLD not in text:
        continue
    text = text.replace(OLD, NEW)
    text = re.sub(r"styles\.css\?v=\d+", "styles.css?v=26", text)
    path.write_text(text, encoding="utf-8", newline="\n")
    print("updated", path.name)
