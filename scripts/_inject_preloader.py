"""Inject site preloader markup into public HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CRITICAL = (
    '  <script id="preloader-boot">'
    "try{if(sessionStorage.getItem('shubh_preloader_seen')==='1')"
    "document.documentElement.classList.remove('is-preload')}catch(e){}"
    "</script>\n"
    '  <style id="preloader-critical">'
    "html.is-preload,html.is-preload body{overflow:hidden}"
    "html:not(.is-preload) .site-preloader{display:none!important}"
    ".site-preloader{position:fixed;inset:0;z-index:10000;display:grid;place-items:center;"
    "padding:1.5rem;background:linear-gradient(165deg,#06354a 0%,#0a4d68 42%,#0078a8 100%);color:#fff}"
    ".site-preloader__inner{display:flex;flex-direction:column;align-items:center;text-align:center;gap:.75rem;width:min(100%,20rem)}"
    ".site-preloader__mark{position:relative;width:7.25rem;height:7.25rem;display:grid;place-items:center}"
    ".site-preloader__mark img{width:4.75rem;height:4.75rem;object-fit:contain;border-radius:50%;background:#fff;padding:.35rem}"
    ".site-preloader__brand{margin:0;font:700 clamp(1.55rem,4vw,2rem)/1.1 Sora,Segoe UI,sans-serif}"
    ".site-preloader__tag{margin:0;font-size:.78rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.78)}"
    ".site-preloader__bar{width:100%;height:3px;margin-top:1rem;border-radius:999px;background:rgba(255,255,255,.18);overflow:hidden}"
    ".site-preloader__bar-fill{display:block;height:100%;width:0;background:#00aeef}"
    ".site-preloader__pct{margin:0;font-size:.88rem;letter-spacing:.08em;color:rgba(255,255,255,.72)}"
    ".site-preloader.is-done{opacity:0;visibility:hidden;pointer-events:none}"
    "</style>\n"
)

PRELOADER = """
  <div class="site-preloader" id="site-preloader" role="status" aria-live="polite" aria-busy="true" aria-label="Loading Shubhshrey Industries">
    <div class="site-preloader__glow" aria-hidden="true"></div>
    <div class="site-preloader__inner">
      <div class="site-preloader__mark">
        <span class="site-preloader__ring" aria-hidden="true"></span>
        <span class="site-preloader__ring site-preloader__ring--delay" aria-hidden="true"></span>
        <img src="assets/logo.png" alt="" width="96" height="96" decoding="async" />
      </div>
      <p class="site-preloader__brand">Bharatweld</p>
      <p class="site-preloader__tag">Shubhshrey Industries</p>
      <div class="site-preloader__bar" aria-hidden="true"><span class="site-preloader__bar-fill"></span></div>
      <p class="site-preloader__pct"><span data-preloader-pct>0</span>%</p>
    </div>
  </div>
""".rstrip() + "\n\n"


def patch(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    if "styles.css" not in text or "main.js" not in text:
        return False

    text = re.sub(r'<html\s+lang="en">', '<html lang="en" class="is-preload">', text, count=1)
    text = re.sub(r"styles\.css\?v=\d+", "styles.css?v=21", text)
    text = re.sub(r"main\.js\?v=\d+", "main.js?v=11", text)

    if 'id="preloader-critical"' not in text:
        text = text.replace("</head>", CRITICAL + "</head>", 1)

    if 'id="site-preloader"' not in text:
        text = re.sub(
            r"(<body[^>]*>\s*)",
            r"\1" + PRELOADER,
            text,
            count=1,
            flags=re.IGNORECASE,
        )

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> None:
    changed = []
    for path in sorted(ROOT.glob("*.html")):
        if patch(path):
            changed.append(path.name)
            print(f"patched {path.name}")
        else:
            print(f"skip {path.name}")
    print(f"changed={len(changed)}")


if __name__ == "__main__":
    main()
