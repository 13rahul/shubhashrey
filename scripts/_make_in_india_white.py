"""Convert Make in India lion to white mark on transparent background."""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "make-in-india.png"
OUT = ROOT / "assets" / "make-in-india.png"
BACKUP = ROOT / "assets" / "make-in-india-original.png"


def main() -> None:
    im = Image.open(SRC).convert("RGBA")
    if not BACKUP.exists():
        im.save(BACKUP)

    w, h = im.size
    px = im.load()
    gray = im.convert("L")
    gp = gray.load()

    # Flood-fill background from corners (near-white)
    bg = Image.new("1", (w, h), 0)
    draw = ImageDraw.Draw(bg)
    # seed corners
    seeds = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    visited = [[False] * w for _ in range(h)]
    stack = []
    for sx, sy in seeds:
        if gp[sx, sy] >= 200:
            stack.append((sx, sy))
            visited[sy][sx] = True

    while stack:
        x, y = stack.pop()
        bg.putpixel((x, y), 1)
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and gp[nx, ny] >= 200:
                visited[ny][nx] = True
                stack.append((nx, ny))

    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    op = out.load()
    for y in range(h):
        for x in range(w):
            if bg.getpixel((x, y)):
                continue  # transparent background
            g = gp[x, y]
            if g < 200:
                # lion body -> white
                op[x, y] = (255, 255, 255, 255)
            else:
                # cutout text / holes -> transparent
                op[x, y] = (0, 0, 0, 0)

    # Trim empty margins
    bbox = out.getbbox()
    if bbox:
        out = out.crop(bbox)

    out.save(OUT)
    print("saved", OUT, out.size)


if __name__ == "__main__":
    main()
