from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = '<p class="site-preloader__brand">BHARATWELD™</p>'
NEW = '<p class="site-preloader__brand">BHARATWELD<span class="brand-tm">™</span></p>'

for path in list(ROOT.glob("*.html")) + list((ROOT / "products").glob("*.html")):
    text = path.read_text(encoding="utf-8")
    if OLD in text:
        path.write_text(text.replace(OLD, NEW), encoding="utf-8")
        print("updated", path.name)

gen = ROOT / "scripts" / "_gen_product_pages.py"
gt = gen.read_text(encoding="utf-8")
if OLD in gt:
    gen.write_text(gt.replace(OLD, NEW), encoding="utf-8")
    print("updated generator")
