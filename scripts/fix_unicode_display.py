#!/usr/bin/env python3
"""Replace punctuation that often renders as empty boxes with ASCII-safe text."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "\u2014": "-",
    "\u2013": "-",
    "\u2026": "...",
    "\u2192": "->",
    "\u2190": "<-",
    "\u00b7": "|",
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u00d7": "x",
    "\u2022": "-",
}

GLOBS = [
    "*.html",
    "css/*.css",
    "js/*.js",
    "admin/**/*.php",
    "admin/**/*.css",
    "admin/**/*.js",
    "admin/**/*.md",
    "api/**/*.php",
    "includes/**/*.php",
    "config/**/*.php",
    "data/**/*.md",
    "scripts/**/*.py",
]


def main() -> None:
    files: list[Path] = []
    for pattern in GLOBS:
        files.extend(ROOT.glob(pattern))
    changed = 0
    for path in sorted(set(files)):
        if not path.is_file() or path.name == Path(__file__).name:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        original = text
        for old, new in REPLACEMENTS.items():
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed += 1
            print(f"updated {path.relative_to(ROOT)}")
    print(f"files changed: {changed}")


if __name__ == "__main__":
    main()
