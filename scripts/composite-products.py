"""Composite real welding rod photos with Bharatweld packaging box."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PACK_DESIGN = ROOT / "assets" / "bharatweld-pack.png"
PACK_PHOTO = ROOT / "assets" / "bharatweld-pack.jpg"
OUT_DIR = ROOT / "assets" / "products"

CANVAS_W, CANVAS_H = 1200, 900
BG = (255, 255, 255)

PRODUCTS = [
    ("e-6013.png", "E-6013", "GENERAL PURPOSE"),
    ("e-7018.png", "E-7018", "LOW HYDROGEN"),
    ("e-308l.png", "E-308L", "STAINLESS STEEL"),
    ("cutting.png", "CAPTAIN CUT", "CUTTING & GOUGING"),
    ("manganese.png", "MANGANESE", "HARDFACING"),
]


def load_font(size: int, bold: bool = False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def crop_pack_box_from_photo() -> Image.Image:
    """Crop the physical Bharatweld box from the reference photo."""
    img = Image.open(PACK_PHOTO).convert("RGBA")
    w, h = img.size
    # Box occupies roughly the left-center of the photo
    left = int(w * 0.06)
    top = int(h * 0.08)
    right = int(w * 0.56)
    bottom = int(h * 0.78)
    box = img.crop((left, top, right, bottom))
    return box


def make_pack_panel(grade: str, subtitle: str) -> Image.Image:
    """Build packaging panel: real box photo + grade badge overlay."""
    box = crop_pack_box_from_photo()
    panel_w = int(CANVAS_W * 0.42)
    panel_h = int(CANVAS_H * 0.88)
    box.thumbnail((panel_w, panel_h), Image.Resampling.LANCZOS)

    panel = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
    x = (panel_w - box.width) // 2
    y = (panel_h - box.height) // 2
    panel.paste(box, (x, y), box if box.mode == "RGBA" else None)

    # Grade badge strip at bottom of box area
    draw = ImageDraw.Draw(panel)
    badge_h = 44
    badge_y = y + box.height - badge_h - 8
    badge_x = x + 8
    badge_w = box.width - 16
    draw.rounded_rectangle(
        (badge_x, badge_y, badge_x + badge_w, badge_y + badge_h),
        radius=8,
        fill=(0, 174, 239, 240),
    )
    grade_font = load_font(22, bold=True)
    sub_font = load_font(11, bold=False)
    draw.text(
        (badge_x + badge_w // 2, badge_y + 12),
        grade,
        fill=(255, 255, 255),
        font=grade_font,
        anchor="mm",
    )
    draw.text(
        (badge_x + badge_w // 2, badge_y + 32),
        subtitle,
        fill=(255, 255, 255),
        font=sub_font,
        anchor="mm",
    )
    return panel


def composite(rod_filename: str, grade: str, subtitle: str) -> None:
    rods_path = OUT_DIR / rod_filename
    rods = Image.open(rods_path).convert("RGBA")

    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), BG)

    pack_panel = make_pack_panel(grade, subtitle)
    pack_x = int(CANVAS_W * 0.04)
    pack_y = (CANVAS_H - pack_panel.height) // 2
    canvas.paste(pack_panel, (pack_x, pack_y), pack_panel)

    rod_area_w = int(CANVAS_W * 0.52)
    rod_area_h = int(CANVAS_H * 0.85)
    rods.thumbnail((rod_area_w, rod_area_h), Image.Resampling.LANCZOS)
    rod_x = int(CANVAS_W * 0.44) + (rod_area_w - rods.width) // 2
    rod_y = (CANVAS_H - rods.height) // 2

    if rods.mode == "RGBA":
        canvas.paste(rods, (rod_x, rod_y), rods)
    else:
        canvas.paste(rods, (rod_x, rod_y))

    out_path = OUT_DIR / rod_filename
    canvas.save(out_path, "PNG", optimize=True)
    print(f"Saved {out_path.name} ({canvas.size[0]}x{canvas.size[1]})")


def main():
    # Keep originals as -rods-only backup on first run
    for filename, _, _ in PRODUCTS:
        src = OUT_DIR / filename
        backup = OUT_DIR / filename.replace(".png", "-rods-only.png")
        if src.exists() and not backup.exists():
            Image.open(src).save(backup)
            print(f"Backup: {backup.name}")

    for filename, grade, subtitle in PRODUCTS:
        composite(filename, grade, subtitle)


if __name__ == "__main__":
    main()
