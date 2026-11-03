from pathlib import Path

from PIL import Image

SRC = Path(__file__).resolve().parents[1] / "assets" / "iso-isi-source.png"
ASSETS = SRC.parent


def is_bg(r: int, g: int, b: int, tol: int = 45) -> bool:
    return abs(r - 0) < tol and abs(g - 176) < 65 and abs(b - 240) < 65


def main() -> None:
    im = Image.open(SRC).convert("RGBA")
    w, h = im.size
    pixels = im.load()
    mask = Image.new("L", im.size, 0)
    mp = mask.load()
    white = Image.new("RGBA", im.size, (0, 0, 0, 0))
    wp = white.load()

    xs: list[int] = []
    ys: list[int] = []
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if is_bg(r, g, b):
                continue
            bright = max(r, g, b)
            if bright < 120:
                continue
            alpha = 255 if bright > 200 else min(255, bright + 30)
            wp[x, y] = (255, 255, 255, alpha)
            mp[x, y] = 255
            xs.append(x)
            ys.append(y)

    print("content bbox", min(xs), min(ys), max(xs), max(ys))

    # Find vertical gap between left/right logos
    empty_cols = []
    for x in range(min(xs), max(xs) + 1):
        if all(mask.getpixel((x, y)) == 0 for y in range(h)):
            empty_cols.append(x)

    center = (min(xs) + max(xs)) // 2
    if empty_cols:
        # Prefer a gap near the middle
        split = min(empty_cols, key=lambda x: abs(x - center))
        # Expand to mid of contiguous empty run around split
        left = split
        right = split
        while left - 1 in empty_cols:
            left -= 1
        while right + 1 in empty_cols:
            right += 1
        split = (left + right) // 2
    else:
        split = center
    print("split_x", split, "empty_cols", len(empty_cols))

    def crop_side(x0: int, x1: int, pad: int = 18) -> Image.Image:
        cxs: list[int] = []
        cys: list[int] = []
        for y in range(h):
            for x in range(x0, x1):
                if mask.getpixel((x, y)):
                    cxs.append(x)
                    cys.append(y)
        box = (
            max(0, min(cxs) - pad),
            max(0, min(cys) - pad),
            min(w, max(cxs) + pad + 1),
            min(h, max(cys) + pad + 1),
        )
        return white.crop(box)

    iso = crop_side(0, split)
    isi = crop_side(split, w)

    iso_path = ASSETS / "iso-9001.png"
    isi_path = ASSETS / "isi-is814.png"
    iso.save(iso_path)
    isi.save(isi_path)
    print("saved", iso_path.name, iso.size)
    print("saved", isi_path.name, isi.size)


if __name__ == "__main__":
    main()
