import re
from pathlib import Path

t = Path("index.html").read_text(encoding="utf-8")
for m in re.finditer(r'brand-tm">(.*?)</span>', t):
    s = m.group(1)
    print([hex(ord(c)) for c in s], repr(s))
print("tm count", t.count("\u2122"))
print("fffd count", t.count("\ufffd"))
