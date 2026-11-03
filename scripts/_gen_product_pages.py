"""Generate static SEO product pages under products/."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "products"
SITE = "https://shubhshrey.com"
CSS_V = "30"
JS_MAIN = "13"
JS_PRODUCTS = "10"
JS_CART = "6"

PRODUCTS = [
    {
        "id": "e-6013",
        "sku": "BW-E6013",
        "name": "E6013 Welding Electrodes",
        "shortName": "E6013",
        "category": "Mild Steel Welding Electrodes",
        "categoryGroup": "mild-steel",
        "tagline": "General-purpose rutile electrode for mild steel fabrication",
        "description": (
            "Bharatweld E6013 is a rutile-coated general-purpose electrode for mild steel. "
            "Smooth arc, easy slag removal, and a clean bead — ideal for gates, grills, "
            "sheet metal, and everyday workshop welding across India."
        ),
        "meta_extra": (
            "Buy Bharatweld E6013 rutile welding electrodes from Shubhshrey Industries, "
            "Baramati. AWS E6013, all-position, AC/DC. Made in India."
        ),
        "benefits": [
            "Smooth, stable arc for everyday fabrication",
            "Easy slag removal and clean bead appearance",
            "All-position welding, especially flat and horizontal",
            "Works on AC or DC power sources",
        ],
        "price": 1900,
        "image": "e-6013.png",
        "rods": "e-6013-rods-only.png",
        "compare": "e-7018",
        "aws": "E6013",
        "coating": "Rutile",
        "positions": "All positions (especially flat & horizontal)",
        "polarity": "AC or DC either polarity",
        "diameters": "2.5 mm, 3.15 mm, 4 mm",
        "amps": [
            {"d": "2.5 mm", "range": "60–90 A", "tip": "Sheet metal, thin gates — keep a short arc."},
            {"d": "3.15 mm", "range": "90–130 A", "tip": "Most common workshop diameter for fabrication."},
            {"d": "4.0 mm", "range": "130–180 A", "tip": "Heavier plate and higher deposit rate."},
        ],
        "industries": ["General fabrication", "Furniture", "Construction", "Repair shops"],
        "applications": [
            "Sheet metal welding",
            "Gate and grill fabrication",
            "Light-duty steel structures",
            "Maintenance and repair",
        ],
    },
    {
        "id": "e-7018",
        "sku": "BW-E7018",
        "name": "E7018 Welding Electrodes",
        "shortName": "E7018",
        "category": "Low Hydrogen Structural Electrodes",
        "categoryGroup": "mild-steel",
        "tagline": "Low-hydrogen electrode for structural and high-strength steel",
        "description": (
            "Bharatweld E7018 (E7018/E7018-1) is a low-hydrogen electrode for high-strength, "
            "crack-resistant welds on structural steel, heavy fabrication, bridges, and "
            "pressure-boundary work where ductility matters."
        ),
        "meta_extra": (
            "Bharatweld E7018 / E7018-1 low-hydrogen welding electrodes by Shubhshrey Industries. "
            "Structural, heavy fabrication, and high-tensile steel. Made in India."
        ),
        "benefits": [
            "Low-hydrogen deposit for crack-resistant welds",
            "High strength and ductility for structural work",
            "Suitable for heavy fabrication and pressure vessels",
            "All-position capability with AC or DC+",
        ],
        "price": 3000,
        "image": "e-7018.png",
        "rods": "e-7018-rods-only.png",
        "compare": "e-6013",
        "aws": "E7018 / E7018-1",
        "coating": "Low hydrogen",
        "positions": "All positions",
        "polarity": "AC or DC+ (DCEP)",
        "diameters": "2.5 mm, 3.15 mm, 4 mm",
        "amps": [
            {"d": "2.5 mm", "range": "70–100 A", "tip": "Thinner structural members; store dry."},
            {"d": "3.15 mm", "range": "100–140 A", "tip": "Standard structural and machinery joints."},
            {"d": "4.0 mm", "range": "140–190 A", "tip": "Heavy sections — keep electrodes dry."},
        ],
        "industries": ["Heavy construction", "Mining", "Oil and gas", "Shipbuilding"],
        "applications": [
            "High-tensile steel",
            "Structural frames and bridges",
            "Heavy machinery parts",
            "Pressure vessels",
        ],
    },
    {
        "id": "e-308l",
        "sku": "BW-E308L",
        "name": "E308L Stainless Steel Electrodes",
        "shortName": "E308L",
        "category": "Stainless Steel Welding Electrodes",
        "categoryGroup": "stainless",
        "tagline": "Stainless electrode for 304/308 grades and corrosion-resistant work",
        "description": (
            "Bharatweld E308L-16 is designed for 18/8 stainless steels including AISI 304L and 308L. "
            "Stable arc, clean bead appearance, and reliable performance for food, chemical, "
            "and architectural stainless applications."
        ),
        "meta_extra": (
            "Bharatweld E308L-16 stainless welding electrodes from Shubhshrey Industries. "
            "For AISI 304L/308L food, chemical, and architectural stainless. Made in India."
        ),
        "benefits": [
            "Extra-low carbon for corrosion-resistant stainless welds",
            "Stable arc and clean bead on 18/8 grades",
            "Ideal for food, chemical, and pharma equipment",
            "All-position welding with AC or DC+",
        ],
        "price": 5000,
        "image": "e-308l.png",
        "rods": "e-308l-rods-only.png",
        "aws": "E308L-16",
        "coating": "Extra low carbon stainless",
        "positions": "All positions",
        "polarity": "AC or DC+",
        "diameters": "2.5 mm, 3.15 mm",
        "amps": [
            {"d": "2.5 mm", "range": "50–80 A", "tip": "Thin stainless sheet — control heat input."},
            {"d": "3.15 mm", "range": "80–110 A", "tip": "Equipment and general stainless fab."},
        ],
        "industries": ["Food processing", "Chemical", "Pharmaceutical", "Architectural stainless"],
        "applications": [
            "AISI 304L and 308L stainless",
            "Food and chemical equipment",
            "Corrosion-resistant fabrication",
            "General stainless steel work",
        ],
    },
    {
        "id": "cutting",
        "sku": "BW-CAPTAIN-CUT",
        "name": "Industrial Cutting Electrodes",
        "shortName": "Captain Cut",
        "category": "Cutting & Gouging Electrodes",
        "categoryGroup": "cutting",
        "tagline": "Captain-Cut electrodes for metal cutting and gouging",
        "description": (
            "Bharatweld Captain-Cut cutting electrodes are for metal severing, piercing, "
            "gouging, and weld removal on mild steel, cast iron, and non-ferrous metals — "
            "a practical tool for maintenance crews and fabrication shops."
        ),
        "meta_extra": (
            "Bharatweld Captain-Cut industrial cutting and gouging electrodes by Shubhshrey Industries. "
            "Cut, pierce, and gouge without oxy-fuel. Made in India."
        ),
        "benefits": [
            "Cut and gouge without oxy-fuel equipment",
            "Works on mild steel, cast iron, and many non-ferrous metals",
            "Useful for piercing, crack gouging, and weld removal",
            "Practical for maintenance and fabrication shops",
        ],
        "price": 2500,
        "image": "cutting.png",
        "rods": "cutting-rods-only.png",
        "aws": "Cutting / gouging type",
        "coating": "Special cutting flux",
        "positions": "Flat, vertical (cutting applications)",
        "polarity": "AC or DC",
        "diameters": "4 mm, 5 mm",
        "amps": [
            {"d": "4.0 mm", "range": "200–300 A", "tip": "Push through plate; keep a long arc for cutting."},
            {"d": "5.0 mm", "range": "250–350 A", "tip": "Faster severing on thicker sections."},
        ],
        "industries": ["Maintenance", "Demolition", "Foundries", "General fabrication"],
        "applications": [
            "Metal cutting and severing",
            "Piercing holes",
            "Gouging cracks before re-weld",
            "Removing old welds and rusty bolts",
        ],
    },
    {
        "id": "manganese",
        "sku": "BW-MN",
        "name": "Manganese Hardfacing Electrodes",
        "shortName": "Manganese",
        "category": "Hardfacing & Wear Resistant Electrodes",
        "categoryGroup": "hardfacing",
        "tagline": "High-manganese overlay for impact and abrasion resistance",
        "description": (
            "Bharatweld manganese hardfacing electrodes deposit wear-resistant overlays on "
            "crushers, excavator parts, railway components, and mining equipment subject to "
            "heavy impact and abrasion in Indian industrial conditions."
        ),
        "meta_extra": (
            "Bharatweld manganese hardfacing electrodes from Shubhshrey Industries. "
            "Wear-resistant overlays for mining, crushers, and railways. Made in India."
        ),
        "benefits": [
            "High-manganese deposit for impact and abrasion resistance",
            "Extends life of crushers, rails, and mining parts",
            "Built for heavy industrial Indian conditions",
            "Suitable for flat and horizontal overlay passes",
        ],
        "price": 20000,
        "image": "manganese.png",
        "rods": "manganese-rods-only.png",
        "aws": "High manganese hardfacing",
        "coating": "Hardfacing flux",
        "positions": "Flat, horizontal (overlay passes)",
        "polarity": "AC or DC+",
        "diameters": "3.15 mm, 4 mm",
        "amps": [
            {"d": "3.15 mm", "range": "100–140 A", "tip": "Build-up passes on worn edges."},
            {"d": "4.0 mm", "range": "140–180 A", "tip": "Higher deposit for crushers and rails."},
        ],
        "industries": ["Mining", "Quarrying", "Railways", "Heavy industry"],
        "applications": [
            "Crusher and mill parts",
            "Rail and track overlays",
            "Wear-resistant hardfacing",
            "Mining equipment repair",
        ],
    },
]

PRELOADER = """  <div class="site-preloader" id="site-preloader" role="status" aria-live="polite" aria-busy="true" aria-label="Loading Shubhshrey Industries">
    <div class="site-preloader__glow" aria-hidden="true"></div>
    <div class="site-preloader__inner">
      <div class="site-preloader__mark">
        <span class="site-preloader__ring" aria-hidden="true"></span>
        <span class="site-preloader__ring site-preloader__ring--delay" aria-hidden="true"></span>
        <img src="../assets/logo.png" alt="" width="96" height="96" decoding="async" />
      </div>
      <p class="site-preloader__brand">Bharatweld</p>
      <p class="site-preloader__tag">Shubhshrey Industries</p>
      <div class="site-preloader__bar" aria-hidden="true"><span class="site-preloader__bar-fill"></span></div>
      <p class="site-preloader__pct"><span data-preloader-pct>0</span>%</p>
    </div>
  </div>"""

PRELOADER_STYLE = """  <script id="preloader-boot">try{if(sessionStorage.getItem('shubh_preloader_seen')==='1')document.documentElement.classList.remove('is-preload')}catch(e){}</script>
  <style id="preloader-critical">html.is-preload,html.is-preload body{overflow:hidden}html:not(.is-preload) .site-preloader{display:none!important}.site-preloader{position:fixed;inset:0;z-index:10000;display:grid;place-items:center;padding:1.5rem;background:linear-gradient(165deg,#06354a 0%,#0a4d68 42%,#0078a8 100%);color:#fff}.site-preloader__inner{display:flex;flex-direction:column;align-items:center;text-align:center;gap:.75rem;width:min(100%,20rem)}.site-preloader__mark{position:relative;width:7.25rem;height:7.25rem;display:grid;place-items:center}.site-preloader__mark img{width:4.75rem;height:4.75rem;object-fit:contain;border-radius:50%;background:#fff;padding:.35rem}.site-preloader__brand{margin:0;font:700 clamp(1.55rem,4vw,2rem)/1.1 Sora,Segoe UI,sans-serif}.site-preloader__tag{margin:0;font-size:.78rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.78)}.site-preloader__bar{width:100%;height:3px;margin-top:1rem;border-radius:999px;background:rgba(255,255,255,.18);overflow:hidden}.site-preloader__bar-fill{display:block;height:100%;width:0;background:#00aeef}.site-preloader__pct{margin:0;font-size:.88rem;letter-spacing:.08em;color:rgba(255,255,255,.72)}.site-preloader.is-done{opacity:0;visibility:hidden;pointer-events:none}</style>"""

FOOTER = """  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <img src="../assets/logo.png" alt="" width="56" height="56" />
        <div>
          <strong>SHUBHSHREY INDUSTRIES PRIVATE LIMITED</strong>
          <p>Bharatweld - Proudly Indian For Indians</p>
          <div class="social-links">
            <a href="https://www.linkedin.com/company/shubhshrey-industries-pvt-ltd/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 114.127 0 2.063 2.063 0 01-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
            <a href="http://www.facebook.com/" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
            <a href="http://www.instagram.com/" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
            <a href="http://www.twitter.com/" target="_blank" rel="noopener noreferrer" aria-label="Twitter"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
          </div>
        </div>
      </div>
      <div>
        <h3>Useful links</h3>
        <ul class="footer-links">
          <li><a href="../shop.html">Shop electrodes</a></li>
          <li><a href="../industries.html">Industries &amp; applications</a></li>
          <li><a href="../about.html">Company profile</a></li>
          <li><a href="../distributor.html">Become our distributor</a></li>
          <li><a href="../contact.html">Contact us</a></li>
        </ul>
      </div>
      <div>
        <h3>Resources</h3>
        <ul class="footer-links">
          <li><a href="../affiliations.html">Affiliations</a></li>
          <li><a href="../approvals.html">Approvals &amp; certifications</a></li>
          <li><a href="../network.html">Our network</a></li>
          <li><a href="../quality-policy.html">Quality policy</a></li>
          <li><a href="../she-policy.html">Safety, health &amp; environment</a></li>
          <li><a href="../welding-process.html">Welding procedures</a></li>
          <li><a href="../assets/brochure/bharatweld-brochure.pdf" download>Download brochure (PDF)</a></li>
        </ul>
      </div>
      <div>
        <h3>Contact</h3>
        <p>2, G-241/4, MIDC Area, Baramati, Katphal, Maharashtra 413133</p>
        <p><a href="mailto:contact@shubhshrey.com">contact@shubhshrey.com</a></p>
        <p><a href="tel:+919168679621">+91-9168679621</a></p>
        <p><a href="https://wa.me/919168679621" target="_blank" rel="noopener noreferrer">WhatsApp</a></p>
      </div>
    </div>
    <div class="container footer-badges" aria-label="Certifications and initiatives">
      <img class="footer-badge--mark footer-badge--mii" src="../assets/make-in-india-white.png?v=2" alt="Make in India" width="140" height="90" loading="lazy" />
      <img class="footer-badge--mark" src="../assets/iso-9001.png" alt="ISO 9001:2015 Certified Company" width="96" height="96" loading="lazy" />
      <img class="footer-badge--mark" src="../assets/isi-is814.png" alt="ISI mark IS 814, licence CM/L-7500353516" width="92" height="102" loading="lazy" />
      <img class="footer-badge--mark footer-badge--msme" src="../assets/msme.png" alt="MSME — Micro, Small & Medium Enterprises" width="160" height="70" loading="lazy" />
    </div>
    <div class="container footer-bottom">
      <div class="footer-bottom-inner">
        <p>&copy; <span id="year"></span> Shubhshrey Industries Private Limited. All rights reserved.</p>
        <p>Developed by <a href="https://fundaking.com/" target="_blank" rel="noopener noreferrer">Fundaking Media</a></p>
      </div>
    </div>
  </footer>"""


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def related_for(p: dict) -> list[dict]:
    return [x for x in PRODUCTS if x["categoryGroup"] == p["categoryGroup"] and x["id"] != p["id"]]


def amp_picker_html(p: dict) -> str:
    amps = p.get("amps") or []
    if not amps:
        return ""
    chips = []
    for i, a in enumerate(amps):
        active = " is-active" if i == 0 else ""
        chips.append(
            f'<button type="button" class="amp-picker__chip{active}" data-amp '
            f'data-amp-range="{esc(a["range"])}" data-amp-tip="{esc(a["tip"])}">{esc(a["d"])}</button>'
        )
    first = amps[0]
    return f"""
            <div class="amp-picker" data-amp-picker>
              <h2 class="product-detail__subhead">Suggested current by diameter</h2>
              <p>Pick a diameter to see a typical amperage window for Bharatweld {esc(p["shortName"])}.</p>
              <div class="amp-picker__chips">
                {"".join(chips)}
              </div>
              <p class="amp-picker__readout"><strong data-amp-range>{esc(first["range"])}</strong></p>
              <p class="amp-picker__tip" data-amp-tip>{esc(first["tip"])}</p>
            </div>"""


def compare_html(p: dict) -> str:
    other_id = p.get("compare")
    if not other_id:
        return ""
    other = next((x for x in PRODUCTS if x["id"] == other_id), None)
    if not other:
        return ""
    return f"""
            <div class="product-compare">
              <h2 class="product-detail__subhead">E6013 vs E7018 — quick pick</h2>
              <table>
                <thead>
                  <tr><th>Factor</th><th>{esc(p["shortName"])}</th><th>{esc(other["shortName"])}</th></tr>
                </thead>
                <tbody>
                  <tr><th scope="row">Coating</th><td>{esc(p["coating"])}</td><td>{esc(other["coating"])}</td></tr>
                  <tr><th scope="row">Best for</th><td>{esc(p["tagline"])}</td><td>{esc(other["tagline"])}</td></tr>
                  <tr><th scope="row">Hydrogen</th><td>{"Low" if "Low" in p["coating"] else "Standard rutile"}</td><td>{"Low" if "Low" in other["coating"] else "Standard rutile"}</td></tr>
                </tbody>
              </table>
              <p><a href="/products/{other["id"]}">Compare with {esc(other["name"])} →</a></p>
            </div>"""


def gallery_html(p: dict, img_path: str) -> str:
    rods = p.get("rods")
    main_alt = f"{p['name']} — Bharatweld welding electrodes packaging"
    if not rods:
        return f'<img src="{img_path}" alt="{esc(main_alt)}" width="1200" height="900" itemprop="image" />'
    rods_path = f"../assets/products/{rods}?v=3"
    rods_alt = f"{p['shortName']} electrode rods — Bharatweld"
    return f"""
            <div data-product-gallery>
              <img src="{img_path}" alt="{esc(main_alt)}" width="1200" height="900" itemprop="image" data-gallery-main />
              <div class="product-gallery">
                <button type="button" class="is-active" data-gallery-thumb data-src="{img_path}" data-alt="{esc(main_alt)}">
                  <img src="{img_path}" alt="" width="240" height="180" loading="lazy" />
                </button>
                <button type="button" data-gallery-thumb data-src="{rods_path}" data-alt="{esc(rods_alt)}">
                  <img src="{rods_path}" alt="" width="240" height="180" loading="lazy" />
                </button>
              </div>
            </div>"""


def render_page(p: dict) -> str:
    url = f"{SITE}/products/{p['id']}"
    img_url = f"{SITE}/assets/products/{p['image']}"
    img_path = f"../assets/products/{p['image']}?v=3"
    desc = p["meta_extra"]
    title = f"{p['name']} | Bharatweld | Shubhshrey Industries"
    related = related_for(p)
    benefits = "".join(f"        <li>{esc(b)}</li>\n" for b in p["benefits"])
    apps = "".join(f"          <li>{esc(a)}</li>\n" for a in p["applications"])
    inds = ", ".join(esc(i) for i in p["industries"])
    amp_block = amp_picker_html(p)
    compare_block = compare_html(p)
    gallery_block = gallery_html(p, img_path)
    related_html = ""
    if related:
        cards = []
        for r in related:
            cards.append(
                f"""        <article class="product-item">
          <a class="product-item__media" href="/products/{r['id']}">
            <img src="../assets/products/{r['image']}?v=3" alt="{esc(r['name'])} - Bharatweld" width="480" height="360" loading="lazy" />
          </a>
          <div class="product-item__body">
            <p class="product-item__cat">{esc(r['category'])}</p>
            <h3 class="product-item__name"><a href="/products/{r['id']}">{esc(r['name'])}</a></h3>
            <p class="product-item__desc">{esc(r['tagline'])}</p>
            <a class="btn btn--ghost btn--sm" href="/products/{r['id']}">View details</a>
          </div>
        </article>"""
            )
        related_html = f"""
      <section class="product-related" aria-labelledby="related-heading">
        <h2 id="related-heading">Related products</h2>
        <div class="product-grid product-grid--related">
{chr(10).join(cards)}
        </div>
      </section>"""

    schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": p["name"],
        "sku": p["sku"],
        "mpn": p["sku"],
        "description": p["description"],
        "image": [img_url],
        "brand": {"@type": "Brand", "name": "Bharatweld"},
        "manufacturer": {
            "@type": "Organization",
            "name": "Shubhshrey Industries Private Limited",
            "url": SITE,
        },
        "category": p["category"],
        "material": p["coating"],
        "offers": {
            "@type": "Offer",
            "url": url,
            "priceCurrency": "INR",
            "price": str(p["price"]),
            "availability": "https://schema.org/InStock",
            "seller": {
                "@type": "Organization",
                "name": "Shubhshrey Industries Private Limited",
            },
        },
    }

    wa = "https://wa.me/919168679621?text=" + quote(
        f"Hello, I need a quote for Bharatweld {p['shortName']} ({p['sku']})."
    )

    return f"""<!DOCTYPE html>
<html lang="en" class="is-preload">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="product" />
  <meta property="og:site_name" content="Shubhshrey Industries" />
  <meta property="og:title" content="{esc(p['name'])} | Bharatweld" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{img_url}" />
  <meta property="product:brand" content="Bharatweld" />
  <meta property="product:retailer_item_id" content="{esc(p['sku'])}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(p['name'])} | Bharatweld" />
  <meta name="twitter:description" content="{esc(desc)}" />
  <meta name="twitter:image" content="{img_url}" />
  <link rel="icon" href="../assets/logo.png" type="image/png" />
  <link rel="preload" href="../assets/logo.png" as="image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/styles.css?v={CSS_V}" />
{PRELOADER_STYLE}
  <script type="application/ld+json">
{json.dumps(schema, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>
{PRELOADER}
  <a class="skip-link" href="#main">Skip to Content</a>

  <header class="site-header">
    <div class="header-inner">
      <a class="logo-link" href="../index.html">
        <img src="../assets/logo.png" alt="Shubhshrey Industries logo" width="52" height="52" />
        <span class="logo-text">Shubhshrey Industries</span>
      </a>
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">
        <span></span><span></span><span></span>
      </button>
      <nav class="site-nav" id="site-nav" aria-label="Primary">
        <a href="../index.html">Home</a>
        <div class="nav-mega" data-nav-mega></div>
        <a href="../industries.html">Industries</a>
        <a href="../about.html">Company Profile</a>
        <a href="../distributor.html">Become a Distributor</a>
        <a href="../contact.html">Contact</a>
        <a class="nav-cart" href="../cart.html">Cart <span class="cart-badge" data-cart-count hidden>0</span></a>
        <a class="nav-whatsapp" href="https://wa.me/919168679621" target="_blank" rel="noopener noreferrer">WhatsApp</a>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="section">
      <div class="container">
        <nav class="product-breadcrumb" aria-label="Breadcrumb">
          <a href="../shop.html">Shop</a>
          <span aria-hidden="true">/</span>
          <a href="../shop.html#category-{esc(p['categoryGroup'])}">{esc(p['category'])}</a>
          <span aria-hidden="true">/</span>
          <span aria-current="page">{esc(p['shortName'])}</span>
        </nav>

        <article class="product-detail" itemscope itemtype="https://schema.org/Product">
          <div class="product-detail__media">
{gallery_block}
          </div>
          <div class="product-detail__info">
            <p class="eyebrow">{esc(p['category'])}</p>
            <h1 itemprop="name">{esc(p['name'])}</h1>
            <p class="product-detail__tagline">{esc(p['tagline'])}</p>
            <p class="product-detail__sku">SKU: <span itemprop="sku">{esc(p['sku'])}</span> | AWS {esc(p['aws'])}</p>
            <p itemprop="description">{esc(p['description'])}</p>

            <h2 class="product-detail__subhead">Key benefits</h2>
            <ul class="product-benefits">
{benefits}            </ul>

            <div class="cta-row">
              <button type="button" class="btn btn--primary" data-buy-now="{esc(p['id'])}">Buy now</button>
              <a class="btn btn--ghost" href="{wa}" target="_blank" rel="noopener noreferrer">WhatsApp quote</a>
              <a class="btn btn--ghost" href="../contact.html">Enquire</a>
            </div>
{amp_block}
{compare_block}
            <table class="spec-table">
              <caption class="visually-hidden">{esc(p['name'])} specifications</caption>
              <tbody>
                <tr><th scope="row">AWS classification</th><td>{esc(p['aws'])}</td></tr>
                <tr><th scope="row">Coating type</th><td>{esc(p['coating'])}</td></tr>
                <tr><th scope="row">Welding positions</th><td>{esc(p['positions'])}</td></tr>
                <tr><th scope="row">Current / polarity</th><td>{esc(p['polarity'])}</td></tr>
                <tr><th scope="row">Diameters</th><td>{esc(p['diameters'])}</td></tr>
                <tr><th scope="row">Industries</th><td>{inds}</td></tr>
              </tbody>
            </table>

            <h2 class="product-detail__subhead">Typical applications</h2>
            <ul class="product-applications">
{apps}            </ul>

            <p class="product-detail__trust">Manufactured by Shubhshrey Industries Private Limited, Baramati — ISO 9001:2015, ISI-marked range, Make in India.</p>
            <p><a href="../shop.html#category-{esc(p['categoryGroup'])}" class="back-link">&larr; Back to {esc(p['category'])}</a></p>
          </div>
        </article>
{related_html}
      </div>
    </section>
  </main>

{FOOTER}

  <a class="wa-fab" href="https://wa.me/message/XG3LL556VT5ME1" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.881 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>

  <script>document.getElementById("year").textContent = new Date().getFullYear();</script>
  <script src="../js/products.js?v={JS_PRODUCTS}"></script>
  <script src="../js/cart.js?v={JS_CART}"></script>
  <script src="../js/main.js?v={JS_MAIN}"></script>
</body>
</html>
"""


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for p in PRODUCTS:
        path = OUT / f"{p['id']}.html"
        path.write_text(render_page(p), encoding="utf-8")
        print("wrote", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
