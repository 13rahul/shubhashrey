"""Remove CAPTAIN CUT from cutting rod photos; stamp BHARATWELD; rebuild composite."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "assets" / "products"
SOURCE = PRODUCTS / "cutting-rods-source.png"
RODS_OUT = PRODUCTS / "cutting-rods-only.png"
PACK_PHOTO = ROOT / "assets" / "bharatweld-pack.jpg"
OUT_COMPOSITE = PRODUCTS / "cutting.png"
CANVAS_W, CANVAS_H = 1200, 900


def load_font(size: int, bold: bool = True):
    for path in (
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def ensure_source() -> Path:
    if SOURCE.exists():
        return SOURCE
    # restore pristine from git once
    import subprocess

    data = subprocess.check_output(
        ["git", "show", "HEAD:assets/products/cutting-rods-only.png"],
        cwd=str(ROOT),
    )
    SOURCE.write_bytes(data)
    return SOURCE


def cover_rod_bands(im: Image.Image) -> Image.Image:
    arr = np.asarray(im.convert("RGB")).astype(np.float32)
    h, w, _ = arr.shape
    out = arr.copy()

    # Approximate vertical rod column ranges (fraction of width)
    rods = [
        (0.08, 0.28),
        (0.30, 0.50),
        (0.52, 0.72),
        (0.74, 0.94),
    ]
    y0, y1 = int(h * 0.20), int(h * 0.70)
    ref0, ref1 = int(h * 0.10), int(h * 0.18)

    for x0f, x1f in rods:
        x0, x1 = int(w * x0f), int(w * x1f)
        band = arr[ref0:ref1, x0:x1]
        # mask out near-white bg
        mask = band.mean(axis=2) < 240
        if mask.any():
            coat = band[mask].mean(axis=0)
        else:
            coat = np.array([175.0, 105.0, 90.0], dtype=np.float32)

        # vertical feather: stronger in center of stamp zone
        for y in range(y0, y1):
            t = (y - y0) / max(1, y1 - y0)
            strength = float(np.sin(np.pi * t) ** 0.7)
            if strength < 0.05:
                continue
            row = out[y, x0:x1].copy()  # (n, 3)
            bg = row.mean(axis=1) > 242
            blend = coat.reshape(1, 3) * strength + row * (1.0 - strength)
            row[~bg] = blend[~bg]
            out[y, x0:x1] = row

    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
    # light blur on stamp zone only
    zone = img.crop((0, y0, w, y1)).filter(ImageFilter.GaussianBlur(1.1))
    img.paste(zone, (0, y0))
    return img


def stamp_bharatweld(im: Image.Image) -> Image.Image:
    w, h = im.size
    font = load_font(max(18, int(w * 0.055)))
    label = "BHARATWELD"
    centers = [int(w * x) for x in (0.18, 0.40, 0.62, 0.84)]
    mid_y = int(h * 0.42)
    base = ImageDraw.Draw(im)
    bbox = base.textbbox((0, 0), label, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]

    for cx in centers:
        txt = Image.new("RGBA", (tw + 10, th + 10), (0, 0, 0, 0))
        ImageDraw.Draw(txt).text((5, 5), label, fill=(255, 255, 255, 230), font=font)
        rotated = txt.rotate(90, expand=True, resample=Image.Resampling.BICUBIC)
        im.paste(rotated, (cx - rotated.width // 2, mid_y - rotated.height // 2), rotated)
    return im


def make_pack_panel() -> Image.Image:
    img = Image.open(PACK_PHOTO).convert("RGBA")
    w, h = img.size
    box = img.crop((int(w * 0.06), int(h * 0.08), int(w * 0.56), int(h * 0.78)))
    panel_w, panel_h = int(CANVAS_W * 0.42), int(CANVAS_H * 0.88)
    box.thumbnail((panel_w, panel_h), Image.Resampling.LANCZOS)
    panel = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
    x = (panel_w - box.width) // 2
    y = (panel_h - box.height) // 2
    panel.paste(box, (x, y), box)
    draw = ImageDraw.Draw(panel)
    badge_h, badge_y, badge_x = 44, y + box.height - 52, x + 8
    badge_w = box.width - 16
    draw.rounded_rectangle(
        (badge_x, badge_y, badge_x + badge_w, badge_y + badge_h),
        radius=8,
        fill=(0, 174, 239, 240),
    )
    draw.text((badge_x + badge_w // 2, badge_y + 12), "CUTTING", fill=(255, 255, 255), font=load_font(20), anchor="mm")
    draw.text(
        (badge_x + badge_w // 2, badge_y + 32),
        "CUTTING & GOUGING",
        fill=(255, 255, 255),
        font=load_font(11, bold=False),
        anchor="mm",
    )
    return panel


def composite(rods: Image.Image) -> Image.Image:
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), (255, 255, 255))
    pack = make_pack_panel()
    canvas.paste(pack, (int(CANVAS_W * 0.04), (CANVAS_H - pack.height) // 2), pack)
    rods_rgba = rods.convert("RGBA")
    area_w, area_h = int(CANVAS_W * 0.52), int(CANVAS_H * 0.85)
    rods_rgba.thumbnail((area_w, area_h), Image.Resampling.LANCZOS)
    rx = int(CANVAS_W * 0.44) + (area_w - rods_rgba.width) // 2
    ry = (CANVAS_H - rods_rgba.height) // 2
    canvas.paste(rods_rgba, (rx, ry), rods_rgba)
    return canvas


def main() -> None:
    src = ensure_source()
    cleaned = cover_rod_bands(Image.open(src).convert("RGB"))
    branded = stamp_bharatweld(cleaned)
    branded.save(RODS_OUT, "PNG", optimize=True)
    composite(branded).save(OUT_COMPOSITE, "PNG", optimize=True)
    print("ok", RODS_OUT.name, OUT_COMPOSITE.name)


if __name__ == "__main__":
    main()
