#!/usr/bin/env python3
"""Repair double-encoded UTF-8 punctuation (browser shows empty boxes).

Cause: UTF-8 bytes for dashes/quotes were decoded as Latin-1 then saved as UTF-8 again.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BYTE_FIXES: list[tuple[bytes, bytes]] = [
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0x94]), b"-"),  # em dash
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0x93]), b"-"),  # en dash
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0xA6]), b"..."),  # ellipsis
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0x99]), b"'"),
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0x98]), b"'"),
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0x9C]), b'"'),
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0x9D]), b'"'),
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0xB9]), b"<"),
    (bytes([0xC3, 0xA2, 0xC2, 0x80, 0xC2, 0xBA]), b">"),
    (bytes([0xC3, 0x82, 0xC2, 0xB7]), b"|"),
    (bytes([0xC3, 0x82]), b""),
    ("\u2014".encode(), b"-"),
    ("\u2013".encode(), b"-"),
    ("\u2026".encode(), b"..."),
    ("\u2192".encode(), b"->"),
    ("\u2190".encode(), b"<-"),
    ("\u00b7".encode(), b"|"),
    ("\u2018".encode(), b"'"),
    ("\u2019".encode(), b"'"),
    ("\u201c".encode(), b'"'),
    ("\u201d".encode(), b'"'),
]

SUFFIXES = {".html", ".css", ".js", ".php", ".md", ".py", ".txt"}


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SUFFIXES:
            continue
        if "node_modules" in path.parts or ".git" in path.parts:
            continue
        data = path.read_bytes()
        original = data
        for old, new in BYTE_FIXES:
            data = data.replace(old, new)
        if data != original:
            path.write_text(data.decode("utf-8", errors="replace"), encoding="utf-8", newline="\n")
            changed += 1
            print(f"fixed {path.relative_to(ROOT)}")
    print(f"files changed: {changed}")


if __name__ == "__main__":
    main()
