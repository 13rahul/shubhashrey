from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD = """    <div class="container footer-badges" aria-label="Certifications and initiatives">
      <img src="assets/make-in-india.png" alt="Make in India" width="160" height="107" loading="lazy" />
      <img src="assets/iso-9001.svg" alt="ISO 9001:2015 Certified Company" width="72" height="72" loading="lazy" />
    </div>"""

NEW = """    <div class="container footer-badges" aria-label="Certifications and initiatives">
      <img src="assets/make-in-india.png" alt="Make in India" width="160" height="107" loading="lazy" />
      <img class="footer-badge--mark" src="assets/iso-9001.png" alt="ISO 9001:2015 Certified Company" width="96" height="96" loading="lazy" />
      <img class="footer-badge--mark" src="assets/isi-is814.png" alt="ISI mark IS 814, licence CM/L-7500353516" width="92" height="102" loading="lazy" />
    </div>"""

# Also handle if already partially updated / different whitespace
OLD_SVG_ONLY = 'src="assets/iso-9001.svg" alt="ISO 9001:2015 Certified Company" width="72" height="72" loading="lazy"'


def main() -> None:
    changed = []
    for path in sorted(ROOT.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        if "footer-badges" not in text:
            continue
        original = text
        if OLD in text:
            text = text.replace(OLD, NEW)
        elif "isi-is814.png" not in text and "iso-9001.svg" in text:
            text = text.replace(
                """      <img src="assets/iso-9001.svg" alt="ISO 9001:2015 Certified Company" width="72" height="72" loading="lazy" />
""",
                """      <img class="footer-badge--mark" src="assets/iso-9001.png" alt="ISO 9001:2015 Certified Company" width="96" height="96" loading="lazy" />
      <img class="footer-badge--mark" src="assets/isi-is814.png" alt="ISI mark IS 814, licence CM/L-7500353516" width="92" height="102" loading="lazy" />
""",
            )
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed.append(path.name)
            print("updated", path.name)
        else:
            print("skip", path.name)
    print("changed", len(changed))


if __name__ == "__main__":
    main()
