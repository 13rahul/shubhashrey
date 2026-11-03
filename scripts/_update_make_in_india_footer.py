from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

OLD = '<img src="assets/make-in-india.png" alt="Make in India" width="160" height="107" loading="lazy" />'
NEW = '<img class="footer-badge--mark footer-badge--mii" src="assets/make-in-india.png" alt="Make in India" width="140" height="90" loading="lazy" />'


def main() -> None:
    for path in list(ROOT.glob("*.html")) + [ROOT / "scripts" / "_footer_resources.html"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if OLD not in text:
            if "footer-badge--mii" in text:
                print("skip", path.name)
            else:
                print("no match", path.name)
            continue
        text = text.replace(OLD, NEW)
        text = re.sub(r"styles\.css\?v=\d+", "styles.css?v=24", text)
        path.write_text(text, encoding="utf-8", newline="\n")
        print("updated", path.name)


if __name__ == "__main__":
    main()
