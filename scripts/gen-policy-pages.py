# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"d:\New folder\htdocs\Subhshrey-industries")

NAV = """      <nav class="site-nav" id="site-nav" aria-label="Primary">
        <a href="index.html">Home</a>
        <div class="nav-mega" data-nav-mega></div>
        <a href="industries.html">Industries</a>
        <a href="about.html">Company Profile</a>
        <a href="distributor.html">Become a Distributor</a>
        <a href="contact.html">Contact</a>
        <a class="nav-cart" href="cart.html">Cart <span class="cart-badge" data-cart-count hidden>0</span></a>
        <a class="nav-whatsapp" href="https://wa.me/919168679621" target="_blank" rel="noopener noreferrer">WhatsApp</a>
      </nav>"""

SOCIAL = """          <div class="social-links">
            <a href="https://www.linkedin.com/company/shubhshrey-industries-pvt-ltd/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 114.127 0 2.063 2.063 0 01-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
            <a href="http://www.facebook.com/" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
            <a href="http://www.instagram.com/" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
            <a href="http://www.twitter.com/" target="_blank" rel="noopener noreferrer" aria-label="Twitter"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
          </div>"""

FOOTER = f"""  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <img src="assets/logo.png" alt="" width="56" height="56" />
        <div>
          <strong>SHUBHSHREY INDUSTRIES PRIVATE LIMITED</strong>
          <p>Bharatweld — Proudly Indian For Indians</p>
{SOCIAL}
        </div>
      </div>
      <div>
        <h3>Useful links</h3>
        <ul class="footer-links">
          <li><a href="shop.html">Shop electrodes</a></li>
          <li><a href="industries.html">Industries &amp; applications</a></li>
          <li><a href="about.html">Company profile</a></li>
          <li><a href="distributor.html">Become our distributor</a></li>
          <li><a href="contact.html">Contact us</a></li>
        </ul>
      </div>
      <div>
        <h3>Resources</h3>
        <ul class="footer-links">
          <li><a href="affiliations.html">Affiliations</a></li>
          <li><a href="approvals.html">Approvals &amp; certifications</a></li>
          <li><a href="network.html">Our network</a></li>
          <li><a href="quality-policy.html">Quality policy</a></li>
          <li><a href="she-policy.html">Safety, health &amp; environment</a></li>
          <li><a href="welding-process.html">Welding procedures</a></li>
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
      <img src="assets/make-in-india.png" alt="Make in India" width="160" height="107" loading="lazy" />
      <img src="assets/iso-9001.svg" alt="ISO 9001:2015 Certified Company" width="72" height="72" loading="lazy" />
    </div>
    <div class="container footer-bottom">
      <div class="footer-bottom-inner">
        <p>&copy; <span id="year"></span> Shubhshrey Industries Private Limited. All rights reserved.</p>
        <p>Developed by <a href="https://fundaking.com/" target="_blank" rel="noopener noreferrer">Fundaking Media</a></p>
      </div>
    </div>
  </footer>"""

WA = """  <a class="wa-fab" href="https://wa.me/message/XG3LL556VT5ME1" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.881 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>"""


def page(title, desc, eyebrow, h1, lead, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | Bharatweld | Shubhshrey Industries</title>
  <meta name="description" content="{desc}" />
  <link rel="icon" href="assets/logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/styles.css?v=14" />
</head>
<body>
  <a class="skip-link" href="#main">Skip to Content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="logo-link" href="index.html">
        <img src="assets/logo.png" alt="Shubhshrey Industries logo" width="52" height="52" />
        <span class="logo-text">Shubhshrey Industries</span>
      </a>
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">
        <span></span><span></span><span></span>
      </button>
{NAV}
    </div>
  </header>
  <main id="main">
    <div class="page-hero">
      <div class="container">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p>{lead}</p>
      </div>
    </div>
    <section class="section">
      <div class="container policy-content reveal">
{body}
      </div>
    </section>
  </main>
{FOOTER}
{WA}
  <script>
    document.getElementById("year").textContent = new Date().getFullYear();
  </script>
  <script src="js/products.js?v=8"></script>
  <script src="js/cart.js?v=4"></script>
  <script src="js/main.js?v=8"></script>
</body>
</html>
"""


pages = {
    "affiliations.html": dict(
        title="Affiliations",
        desc="Affiliations and industry initiatives of Shubhshrey Industries — Bharatweld, Make in India, and ISO 9001:2015.",
        eyebrow="Company",
        h1="Affiliations",
        lead="How Shubhshrey Industries and Bharatweld align with national manufacturing initiatives and quality frameworks.",
        body="""        <p>Shubhshrey Industries Private Limited manufactures Bharatweld welding electrodes from MIDC Baramati, Maharashtra. Our affiliations reflect a commitment to Indian manufacturing, certified quality systems, and practical support for fabricators, dealers, and industrial buyers.</p>
        <div class="policy-cards">
          <article>
            <h2>Make in India</h2>
            <p>Bharatweld electrodes are manufactured in India for Indian workshops — Proudly Indian For Indians. We support domestic fabrication, construction, and maintenance supply chains with locally produced consumables.</p>
          </article>
          <article>
            <h2>ISO 9001:2015</h2>
            <p>We operate as an ISO 9001:2015 certified company, maintaining documented quality processes from raw materials through production, inspection, and dispatch.</p>
          </article>
          <article>
            <h2>Industry partners</h2>
            <p>We work with distributors, dealers, hardware traders, and welding shops across India. Partnership is built on reliable supply, clear communication, and shared growth — see <a href="distributor.html">Become our distributor</a>.</p>
          </article>
          <article>
            <h2>Customer industries</h2>
            <p>Our electrodes serve construction, general fabrication, stainless work, maintenance, mining repair, and farm equipment — view <a href="industries.html">industries &amp; applications</a>.</p>
          </article>
        </div>
        <div class="cta-row">
          <a class="btn btn--primary" href="about.html">Company profile</a>
          <a class="btn btn--ghost" href="contact.html">Contact us</a>
        </div>""",
    ),
    "approvals.html": dict(
        title="Approvals & Certifications",
        desc="Approvals and certifications for Bharatweld electrodes — ISO 9001:2015 and electrode classifications from Shubhshrey Industries.",
        eyebrow="Quality",
        h1="Approvals &amp; certifications",
        lead="Standards and certifications that guide Bharatweld manufacturing and product identification.",
        body="""        <p>Shubhshrey Industries manufactures electrodes to recognised welding electrode classifications used across Indian industry. Our plant quality system is certified to ISO 9001:2015.</p>
        <h2>Company certification</h2>
        <ul class="policy-list">
          <li><strong>ISO 9001:2015</strong> — Certified quality management system for manufacturing of welding electrodes</li>
        </ul>
        <h2>Product classifications</h2>
        <p>Bharatweld grades are identified by industry-standard electrode classifications used by fabricators and inspectors:</p>
        <ul class="policy-list">
          <li><strong>E6013</strong> — General-purpose rutile electrodes for mild steel</li>
          <li><strong>E7018 / E7018-1</strong> — Low-hydrogen electrodes for structural and high-strength work</li>
          <li><strong>E308L-16</strong> — Stainless steel electrodes for 304/308-type applications</li>
          <li><strong>Cutting electrodes</strong> — Captain-Cut industrial cutting and gouging</li>
          <li><strong>Manganese hardfacing</strong> — Wear-resistant overlay electrodes</li>
        </ul>
        <p>For detailed applications and specifications, see our <a href="shop.html">product catalogue</a> and <a href="welding-process.html">welding procedures</a> guide.</p>
        <div class="cta-row">
          <a class="btn btn--primary" href="shop.html">View products</a>
          <a class="btn btn--ghost" href="quality-policy.html">Quality policy</a>
        </div>""",
    ),
    "network.html": dict(
        title="Our Network",
        desc="Bharatweld dealer and distributor network across India — partner with Shubhshrey Industries from Baramati.",
        eyebrow="Distribution",
        h1="Our network",
        lead="A growing dealer and distributor network supplying Bharatweld electrodes to workshops and job sites across India.",
        body="""        <p>Welding consumables must be available where fabricators work — from tier-2 towns to major industrial corridors. Shubhshrey Industries supports a network of distributors, dealers, and channel partners who stock Bharatweld grades and serve local customers with reliable delivery.</p>
        <h2>How our network works</h2>
        <div class="policy-cards">
          <article>
            <h3>Manufacturing hub</h3>
            <p>Electrodes are produced at our MIDC Baramati facility and packed for dispatch to dealers and industrial buyers nationwide.</p>
          </article>
          <article>
            <h3>Dealers &amp; distributors</h3>
            <p>Authorised partners stock E6013, E7018, E308L, cutting, and hardfacing grades for wholesale and retail supply.</p>
          </article>
          <article>
            <h3>End users</h3>
            <p>Fabrication shops, contractors, maintenance teams, and plant stores source Bharatweld through our partners or direct enquiry.</p>
          </article>
        </div>
        <h2>Join the network</h2>
        <p>If you deal in welding consumables or hardware and want to represent Bharatweld in your territory, apply through our distributor form. We review applications and respond on WhatsApp.</p>
        <div class="cta-row">
          <a class="btn btn--primary" href="distributor.html">Become our distributor</a>
          <a class="btn btn--ghost" href="contact.html">Contact sales</a>
        </div>""",
    ),
    "quality-policy.html": dict(
        title="Quality Policy",
        desc="Quality policy of Shubhshrey Industries — ISO 9001:2015 commitment for Bharatweld welding electrodes.",
        eyebrow="Quality",
        h1="Quality policy",
        lead="Our commitment to consistent electrode quality, customer satisfaction, and continual improvement.",
        body="""        <p>Shubhshrey Industries Private Limited is committed to manufacturing Bharatweld welding electrodes that meet customer requirements through a management system aligned with <strong>ISO 9001:2015</strong>.</p>
        <h2>We achieve this by</h2>
        <ul class="policy-list">
          <li>Commitment, training, and excellence among our people</li>
          <li>Continual improvement of products and manufacturing processes</li>
          <li>Setting and reviewing measurable quality objectives</li>
          <li>Adhering to applicable statutory and regulatory requirements</li>
          <li>Producing electrodes in a safe, healthy workplace for customers, suppliers, and society</li>
        </ul>
        <h2>Priority objectives</h2>
        <ul class="policy-list">
          <li><strong>Customer satisfaction</strong> — electrodes that perform as expected on the job site</li>
          <li><strong>On-time delivery</strong> — reliable dispatch from Baramati to partners and buyers</li>
          <li><strong>Consistent product quality</strong> — batch-to-batch stability across Bharatweld grades</li>
        </ul>
        <p>Quality objectives are communicated across our supply chain. Effectiveness is monitored by management so we can improve day-to-day working and the products that leave our plant under the Bharatweld name.</p>
        <p class="policy-signoff"><strong>Shubhshrey Industries Private Limited</strong><br />Directors — Sourabh Bothara &amp; Nikhil Sancheti</p>
        <div class="cta-row">
          <a class="btn btn--primary" href="approvals.html">Approvals &amp; certifications</a>
          <a class="btn btn--ghost" href="about.html">Company profile</a>
        </div>""",
    ),
    "she-policy.html": dict(
        title="Safety, Health & Environment Policy",
        desc="Safety, health and environment policy of Shubhshrey Industries — responsible manufacturing of Bharatweld electrodes in Baramati.",
        eyebrow="Responsibility",
        h1="Safety, health &amp; environment",
        lead="Protecting our people, our community in Baramati, and the environment around our manufacturing operations.",
        body="""        <p>Shubhshrey Industries believes quality manufacturing includes a safe workplace and responsible environmental practice. This policy guides how we produce Bharatweld electrodes at MIDC Baramati.</p>
        <h2>Safety</h2>
        <ul class="policy-list">
          <li>Maintain safe working conditions on the shop floor and in warehouses</li>
          <li>Train employees on equipment handling, PPE, and emergency procedures</li>
          <li>Identify and reduce workplace hazards through regular review</li>
        </ul>
        <h2>Health</h2>
        <ul class="policy-list">
          <li>Support employee wellbeing and hygiene in manufacturing areas</li>
          <li>Control dust, heat, and process exposure with practical shop-floor measures</li>
          <li>Encourage reporting of incidents so we can prevent recurrence</li>
        </ul>
        <h2>Environment</h2>
        <ul class="policy-list">
          <li>Use resources efficiently and minimise waste where practicable</li>
          <li>Handle materials and packaging responsibly through production and dispatch</li>
          <li>Comply with applicable environmental regulations for our industrial operations</li>
        </ul>
        <p>We produce high-quality electrodes while aiming for a workplace that is safe for our team and considerate of the community and environment around our plant.</p>
        <p class="policy-signoff"><strong>Shubhshrey Industries Private Limited</strong><br />MIDC Baramati, Maharashtra</p>
        <div class="cta-row">
          <a class="btn btn--primary" href="quality-policy.html">Quality policy</a>
          <a class="btn btn--ghost" href="contact.html">Contact us</a>
        </div>""",
    ),
}

for fname, meta in pages.items():
    (ROOT / fname).write_text(page(**meta), encoding="utf-8")
    print("Wrote", fname)

(ROOT / "scripts").mkdir(exist_ok=True)
(ROOT / "scripts" / "_footer_resources.html").write_text(FOOTER, encoding="utf-8")
print("Footer template saved")
