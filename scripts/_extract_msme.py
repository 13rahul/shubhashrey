from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "msme-source.png"
OUT = ROOT / "assets" / "msme.png"


def main() -> None:
    im = Image.open(SRC).convert("RGBA")
    w, h = im.size
    px = im.load()
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    op = out.load()
    xs: list[int] = []
    ys: list[int] = []

    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            # black / near-black background -> transparent
            if r < 40 and g < 40 and b < 40:
                continue
            bright = max(r, g, b)
            if bright < 120:
                continue
            # keep white mark
            alpha = 255 if bright > 200 else min(255, bright + 40)
            op[x, y] = (255, 255, 255, alpha)
            xs.append(x)
            ys.append(y)

    pad = 12
    box = (
        max(0, min(xs) - pad),
        max(0, min(ys) - pad),
        min(w, max(xs) + pad + 1),
        min(h, max(ys) + pad + 1),
    )
    cropped = out.crop(box)
    cropped.save(OUT)
    print("saved", OUT, cropped.size)


if __name__ == "__main__":
    main()
