from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOT = (
    '  <script id="preloader-boot">'
    "try{if(sessionStorage.getItem('shubh_preloader_seen')==='1')"
    "document.documentElement.classList.remove('is-preload')}catch(e){}"
    "</script>\n"
)
EXTRA = "html:not(.is-preload) .site-preloader{display:none!important}"

for path in sorted(ROOT.glob("*.html")):
    text = path.read_text(encoding="utf-8")
    if 'id="site-preloader"' not in text:
        continue
    if 'id="preloader-boot"' not in text:
        text = text.replace(
            '<style id="preloader-critical">',
            BOOT + '  <style id="preloader-critical">',
            1,
        )
    if "html:not(.is-preload)" not in text:
        text = text.replace(
            "html.is-preload,html.is-preload body{overflow:hidden}",
            "html.is-preload,html.is-preload body{overflow:hidden}" + EXTRA,
            1,
        )
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"updated {path.name}")
