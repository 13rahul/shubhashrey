# -*- coding: utf-8 -*-
"""Generate Bharatweld / Shubhshrey Industries brand PDF brochure."""
from pathlib import Path
from fpdf import FPDF
from PIL import Image

ROOT = Path(r"d:\New folder\htdocs\Subhshrey-industries")
OUT_DIR = ROOT / "assets" / "brochure"
OUT_PDF = OUT_DIR / "bharatweld-brochure.pdf"
FONTS = Path(r"C:\Windows\Fonts")

# Brand tokens from css/styles.css
BRAND = (0, 174, 239)       # #00AEEF
BRAND_DARK = (0, 144, 200)  # #0090C8
BRAND_DEEP = (0, 120, 168)  # #0078A8
INK = (13, 58, 82)          # #0D3A52
MUTED = (74, 100, 120)      # #4A6478
SURFACE = (244, 251, 254)   # #F4FBFE
WHITE = (255, 255, 255)
LINE = (200, 230, 242)

PRODUCTS = [
    {
        "name": "E6013 Welding Electrodes",
        "aws": "E6013",
        "cat": "Mild Steel | General Purpose",
        "tag": "Rutile electrode for gates, grills, sheet metal & everyday fabrication.",
        "specs": "AC/DC | All positions | 2.5 / 3.15 / 4 mm",
        "image": ROOT / "assets/products/e-6013.png",
    },
    {
        "name": "E7018 Welding Electrodes",
        "aws": "E7018 / E7018-1",
        "cat": "Low Hydrogen | Structural",
        "tag": "High-strength, crack-resistant welds for heavy fabrication & structures.",
        "specs": "AC/DC+ | All positions | 2.5 / 3.15 / 4 mm",
        "image": ROOT / "assets/products/e-7018.png",
    },
    {
        "name": "E308L Stainless Electrodes",
        "aws": "E308L-16",
        "cat": "Stainless Steel",
        "tag": "For 304/308 stainless - food, chemical & architectural work.",
        "specs": "AC/DC+ | All positions | 2.5 / 3.15 mm",
        "image": ROOT / "assets/products/e-308l.png",
    },
    {
        "name": "Industrial Cutting Electrodes",
        "aws": "Captain Cut",
        "cat": "Cutting & Gouging",
        "tag": "Metal cutting, piercing & gouging without oxy-fuel equipment.",
        "specs": "AC/DC | 4 / 5 mm",
        "image": ROOT / "assets/products/cutting.png",
    },
    {
        "name": "Manganese Hardfacing",
        "aws": "Hardfacing",
        "cat": "Wear Resistant Overlays",
        "tag": "Impact & abrasion resistance for crushers, rails & mining equipment.",
        "specs": "AC/DC+ | Flat / horizontal | 3.15 / 4 mm",
        "image": ROOT / "assets/products/manganese.png",
    },
]

VALUES = [
    ("Quality", "Consistent electrode performance under ISO 9001:2015 processes."),
    ("Innovation", "Continuous improvement for Indian workshop conditions."),
    ("Customer Satisfaction", "Responsive service and electrodes welders can trust."),
    ("Employee Involvement", "Skilled teams who take pride in every Bharatweld box."),
    ("Responsibility to Society", "Make in India manufacturing from MIDC Baramati."),
    ("Dealers as Partners", "Long-term relationships with distributors nationwide."),
]


class Brochure(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=False)
        self.add_font("Body", "", str(FONTS / "segoeui.ttf"))
        self.add_font("Body", "B", str(FONTS / "segoeuib.ttf"))
        self.add_font("Body", "I", str(FONTS / "segoeuii.ttf"))

    def brand_header_bar(self, title=""):
        self.set_fill_color(*BRAND)
        self.rect(0, 0, 210, 14, "F")
        self.set_fill_color(*BRAND_DEEP)
        self.rect(0, 14, 210, 1.2, "F")
        if title:
            self.set_xy(14, 3.5)
            self.set_text_color(*WHITE)
            self.set_font("Body", "B", 9)
            self.cell(0, 6, title, align="L")
            self.set_xy(120, 3.5)
            self.cell(76, 6, "BHARATWELD  |  Proudly Indian For Indians", align="R")

    def brand_footer(self, page_label=""):
        self.set_fill_color(*BRAND_DEEP)
        self.rect(0, 287, 210, 10, "F")
        self.set_xy(14, 289.5)
        self.set_text_color(*WHITE)
        self.set_font("Body", "", 7.5)
        self.cell(120, 5, "Shubhshrey Industries Pvt. Ltd.  |  MIDC Baramati  |  +91-9168679621")
        self.set_xy(140, 289.5)
        self.cell(56, 5, page_label or f"Page {self.page_no()}", align="R")

    def section_title(self, text, y=None):
        if y is not None:
            self.set_y(y)
        self.set_text_color(*BRAND_DEEP)
        self.set_font("Body", "B", 16)
        self.cell(0, 8, text)
        self.ln()
        self.set_draw_color(*BRAND)
        self.set_line_width(0.6)
        y2 = self.get_y()
        self.line(14, y2, 55, y2)
        self.ln(4)


def draw_cover(pdf: Brochure):
    pdf.add_page()
    # Full brand field
    pdf.set_fill_color(*BRAND_DEEP)
    pdf.rect(0, 0, 210, 297, "F")
    pdf.set_fill_color(*BRAND)
    pdf.rect(0, 0, 210, 118, "F")
    # Diagonal accent
    pdf.set_fill_color(*BRAND_DARK)
    pdf.polygon([(0, 100), (210, 100), (210, 130), (0, 118)], style="F")

    logo = ROOT / "assets/logo.png"
    if logo.exists():
        # White circle behind logo
        pdf.set_fill_color(*WHITE)
        pdf.ellipse(78, 22, 54, 54, "F")
        pdf.image(str(logo), x=83, y=27, w=44, h=44)

    pdf.set_y(88)
    pdf.set_text_color(*WHITE)
    pdf.set_font("Body", "B", 36)
    pdf.cell(0, 14, "BHARATWELD", align="C")
    pdf.ln()
    pdf.set_font("Body", "I", 13)
    pdf.cell(0, 8, "Proudly Indian For Indians", align="C")
    pdf.ln()

    pdf.set_y(145)
    pdf.set_font("Body", "B", 20)
    pdf.cell(0, 10, "Welding Electrodes", align="C")
    pdf.ln()
    pdf.set_font("Body", "", 12)
    pdf.cell(0, 7, "Product Brochure", align="C")
    pdf.ln()

    pdf.set_y(175)
    pdf.set_font("Body", "", 11)
    for line in (
        "ISO 9001:2015 Certified Manufacturer",
        "Shubhshrey Industries Private Limited",
        "MIDC Baramati, Maharashtra, India",
    ):
        pdf.cell(0, 7, line, align="C")
        pdf.ln()

    # Traits strip
    traits = [
        "More metal recovery",
        "Eye friendly",
        "Less smoke & spatter",
        "Less power consumption",
        "Easy slag removal",
    ]
    pdf.set_y(215)
    pdf.set_fill_color(*WHITE)
    pdf.rect(14, 212, 182, 42, "F")
    pdf.set_text_color(*BRAND_DEEP)
    pdf.set_font("Body", "B", 9)
    pdf.set_xy(14, 216)
    pdf.cell(182, 6, "BHARATWELD ELECTRODE CHARACTERISTICS", align="C")
    pdf.ln()
    pdf.set_font("Body", "", 8.5)
    pdf.set_text_color(*INK)
    x0 = 20
    for i, t in enumerate(traits):
        col = i % 3
        row = i // 3
        pdf.set_xy(x0 + col * 60, 226 + row * 10)
        pdf.set_fill_color(*BRAND)
        pdf.ellipse(x0 + col * 60, 228.5 + row * 10, 2.2, 2.2, "F")
        pdf.set_xy(x0 + col * 60 + 5, 226 + row * 10)
        pdf.cell(52, 6, t)

    pdf.set_y(262)
    pdf.set_text_color(*WHITE)
    pdf.set_font("Body", "", 9)
    pdf.cell(0, 5, "www.shubhshrey.com  |  contact@shubhshrey.com  |  +91-9168679621", align="C")
    pdf.ln()
    pdf.cell(0, 5, "Become our distributor  |  WhatsApp +91 91686 79621", align="C")
    pdf.ln()


def draw_about(pdf: Brochure):
    pdf.add_page()
    pdf.brand_header_bar("COMPANY PROFILE")
    pdf.set_margins(14, 20, 14)
    pdf.set_y(22)

    pdf.section_title("Who we are", 22)
    pdf.set_text_color(*INK)
    pdf.set_font("Body", "", 10)
    about = (
        "Shubhshrey Industries Private Limited is an ISO 9001:2015 certified manufacturer of welding "
        "electrodes, operating from the Maharashtra Industrial Development Corporation (MIDC) area in "
        "Baramati. Under our Bharatweld brand - Proudly Indian For Indians - we supply quality welding "
        "consumables to fabrication shops, contractors, distributors, and industrial buyers across India."
    )
    pdf.multi_cell(182, 5.2, about)
    pdf.ln(3)

    # Facility box
    pdf.set_fill_color(*SURFACE)
    pdf.set_draw_color(*LINE)
    y = pdf.get_y()
    pdf.rect(14, y, 182, 28, "FD")
    pdf.set_xy(18, y + 4)
    pdf.set_font("Body", "B", 10)
    pdf.set_text_color(*BRAND_DEEP)
    pdf.cell(0, 5, "Manufacturing facility")
    pdf.ln()
    pdf.set_x(18)
    pdf.set_font("Body", "", 9)
    pdf.set_text_color(*INK)
    pdf.multi_cell(
        174,
        4.5,
        "2, G-241/4, Maharashtra Industrial Development Corporation Area, Baramati, Katphal, Maharashtra 413133",
    )
    pdf.ln(6)

    pdf.section_title("Our values")
    # 2x3 value cards
    start_y = pdf.get_y()
    card_w, card_h = 88, 28
    for i, (title, text) in enumerate(VALUES):
        col, row = i % 2, i // 2
        x = 14 + col * (card_w + 6)
        y = start_y + row * (card_h + 4)
        pdf.set_fill_color(*WHITE)
        pdf.set_draw_color(*LINE)
        pdf.rect(x, y, card_w, card_h, "FD")
        pdf.set_fill_color(*BRAND)
        pdf.rect(x, y, card_w, 1.8, "F")
        pdf.set_xy(x + 4, y + 5)
        pdf.set_font("Body", "B", 9.5)
        pdf.set_text_color(*BRAND_DEEP)
        pdf.cell(card_w - 8, 5, title)
        pdf.ln()
        pdf.set_x(x + 4)
        pdf.set_font("Body", "", 8)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(card_w - 8, 3.8, text)

    # Directors
    pdf.set_y(start_y + 3 * (card_h + 4) + 4)
    pdf.section_title("Leadership")
    pdf.set_font("Body", "", 10)
    pdf.set_text_color(*INK)
    directors = [
        ("Sourabh Bothara", "Director", "Saurabh@shubhashrey.com"),
        ("Nikhil Sancheti", "Director", "Nikhil@Shubhashrey.com"),
    ]
    y = pdf.get_y()
    for i, (name, role, email) in enumerate(directors):
        x = 14 + i * 94
        pdf.set_fill_color(*SURFACE)
        pdf.rect(x, y, 88, 26, "F")
        pdf.set_xy(x + 5, y + 5)
        pdf.set_font("Body", "B", 11)
        pdf.set_text_color(*INK)
        pdf.cell(78, 5, name)
        pdf.ln()
        pdf.set_x(x + 5)
        pdf.set_font("Body", "", 8.5)
        pdf.set_text_color(*BRAND_DARK)
        pdf.cell(78, 5, role)
        pdf.ln()
        pdf.set_x(x + 5)
        pdf.set_text_color(*MUTED)
        pdf.cell(78, 5, email)

    # Badges
    pdf.set_y(268)
    mii = ROOT / "assets/make-in-india.png"
    if mii.exists():
        pdf.image(str(mii), x=55, y=262, h=18)
    pdf.set_xy(115, 266)
    pdf.set_font("Body", "B", 8)
    pdf.set_text_color(*BRAND_DEEP)
    pdf.cell(70, 5, "ISO 9001:2015 Certified Company")
    pdf.ln()
    pdf.set_x(115)
    pdf.set_font("Body", "", 7.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(70, 4, "Make in India manufacturer")

    pdf.brand_footer("02  |  Company")


def draw_product_pages(pdf: Brochure):
    # Page with first 3 products
    pdf.add_page()
    pdf.brand_header_bar("PRODUCT RANGE")
    pdf.set_y(22)
    pdf.section_title("Bharatweld electrodes")
    pdf.set_font("Body", "", 9.5)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(
        182,
        4.8,
        "Five electrode lines manufactured by Shubhshrey Industries - welding, stainless, cutting, and hardfacing grades for Indian industry.",
    )
    pdf.ln(3)

    def product_card(p, x, y, w=88, h=108):
        pdf.set_fill_color(*WHITE)
        pdf.set_draw_color(*LINE)
        pdf.rect(x, y, w, h, "FD")
        pdf.set_fill_color(*BRAND)
        pdf.rect(x, y, w, 2, "F")
        img_path = p["image"]
        if img_path.exists():
            try:
                with Image.open(img_path) as im:
                    iw, ih = im.size
                max_h = 52
                disp_w = max_h * (iw / ih)
                disp_w = min(disp_w, w - 10)
                pdf.image(str(img_path), x=x + (w - disp_w) / 2, y=y + 5, h=max_h)
            except Exception:
                pass
        ty = y + 60
        pdf.set_xy(x + 4, ty)
        pdf.set_font("Body", "B", 7)
        pdf.set_text_color(*BRAND_DARK)
        pdf.cell(w - 8, 4, p["aws"].upper())
        pdf.set_xy(x + 4, ty + 5)
        pdf.set_font("Body", "B", 9)
        pdf.set_text_color(*INK)
        pdf.multi_cell(w - 8, 4.2, p["name"])
        pdf.set_x(x + 4)
        pdf.set_font("Body", "", 7.5)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(w - 8, 3.6, p["cat"])
        pdf.set_x(x + 4)
        pdf.set_text_color(*INK)
        pdf.multi_cell(w - 8, 3.6, p["tag"])
        pdf.set_x(x + 4)
        pdf.set_font("Body", "", 7)
        pdf.set_text_color(*BRAND_DEEP)
        pdf.multi_cell(w - 8, 3.4, p["specs"])

    product_card(PRODUCTS[0], 14, 48)
    product_card(PRODUCTS[1], 108, 48)
    product_card(PRODUCTS[2], 61, 162)
    pdf.brand_footer("03  |  Products")

    pdf.add_page()
    pdf.brand_header_bar("PRODUCT RANGE")
    pdf.set_y(22)
    pdf.section_title("Cutting & hardfacing")
    product_card(PRODUCTS[3], 14, 42, w=88, h=112)
    product_card(PRODUCTS[4], 108, 42, w=88, h=112)

    pdf.set_y(165)
    pdf.section_title("Industries we serve")
    industries = [
        "Construction & infrastructure",
        "Manufacturing & fabrication",
        "Agriculture & farm equipment",
        "Maintenance & repair",
        "Mining & heavy industry",
        "Food, chemical & stainless",
    ]
    pdf.set_font("Body", "", 9)
    y = pdf.get_y()
    for i, ind in enumerate(industries):
        col, row = i % 2, i // 2
        x = 14 + col * 94
        yy = y + row * 9
        pdf.set_fill_color(*SURFACE)
        pdf.rect(x, yy, 90, 7.5, "F")
        pdf.set_xy(x + 3, yy + 1.2)
        pdf.set_text_color(*INK)
        pdf.cell(84, 5, ">  " + ind)

    pdf.set_fill_color(*BRAND)
    pdf.rect(14, 220, 182, 52, "F")
    pdf.set_xy(20, 226)
    pdf.set_text_color(*WHITE)
    pdf.set_font("Body", "B", 14)
    pdf.cell(0, 7, "Partner with Bharatweld")
    pdf.ln()
    pdf.set_x(20)
    pdf.set_font("Body", "", 9.5)
    pdf.multi_cell(
        170,
        4.5,
        "Shop electrodes, become our distributor, or send an enquiry on WhatsApp.\n"
        "Email: contact@shubhshrey.com  |  Phone / WhatsApp: +91-9168679621\n"
        "Directors: Sourabh Bothara | Nikhil Sancheti",
    )
    pdf.set_xy(20, 255)
    pdf.set_font("Body", "B", 9)
    pdf.cell(0, 5, "www.shubhshrey.com  |  distributor applications welcome")

    pdf.brand_footer("04  |  Products & Contact")


def draw_back_cover(pdf: Brochure):
    pdf.add_page()
    pdf.set_fill_color(*BRAND_DEEP)
    pdf.rect(0, 0, 210, 297, "F")
    pdf.set_fill_color(*BRAND)
    pdf.rect(0, 0, 210, 50, "F")

    logo = ROOT / "assets/logo.png"
    if logo.exists():
        pdf.set_fill_color(*WHITE)
        pdf.ellipse(88, 12, 34, 34, "F")
        pdf.image(str(logo), x=91, y=15, w=28, h=28)

    pdf.set_y(70)
    pdf.set_text_color(*WHITE)
    pdf.set_font("Body", "B", 28)
    pdf.cell(0, 12, "BHARATWELD", align="C")
    pdf.ln()
    pdf.set_font("Body", "I", 12)
    pdf.cell(0, 8, "Proudly Indian For Indians", align="C")
    pdf.ln()

    pdf.set_y(110)
    pdf.set_font("Body", "B", 12)
    pdf.cell(0, 7, "SHUBHSHREY INDUSTRIES PRIVATE LIMITED", align="C")
    pdf.ln()
    pdf.set_font("Body", "", 10)
    pdf.ln(4)
    for line in (
        "2, G-241/4, MIDC Area, Baramati,",
        "Katphal, Maharashtra 413133",
        "",
        "contact@shubhshrey.com",
        "+91-9168679621",
        "WhatsApp: +91 91686 79621",
        "",
        "ISO 9001:2015 Certified",
        "Make in India",
    ):
        pdf.cell(0, 6, line, align="C")
        pdf.ln()

    pdf.set_y(230)
    pdf.set_font("Body", "B", 11)
    pdf.cell(0, 6, "E6013  |  E7018  |  E308L  |  Cutting  |  Manganese", align="C")
    pdf.ln()
    pdf.set_font("Body", "", 9)
    pdf.cell(0, 6, "Welding electrodes manufactured for Indian industry", align="C")
    pdf.ln()

    pdf.set_y(270)
    pdf.set_font("Body", "", 8)
    pdf.cell(0, 5, "(c) Shubhshrey Industries Private Limited. All rights reserved.", align="C")
    pdf.ln()


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf = Brochure()
    draw_cover(pdf)
    draw_about(pdf)
    draw_product_pages(pdf)
    draw_back_cover(pdf)
    pdf.output(str(OUT_PDF))
    print(f"Wrote {OUT_PDF} ({OUT_PDF.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
