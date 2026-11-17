"""Normalize brand display to BHARATWELD™ without touching file paths."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTS = {".html", ".js", ".py", ".xml", ".txt", ".svg", ".css"}
SKIP_DIR_NAMES = {".git", "node_modules", "storage", "admin"}


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIR_NAMES:
        return True
    if "assets" in path.parts and path.suffix.lower() != ".svg":
        return True
    if path.name == "_brand_tm.py":
        return True
    return path.suffix.lower() not in EXTS


def transform(text: str) -> str:
    masks: list[str] = []

    def mask(m: re.Match[str]) -> str:
        masks.append(m.group(0))
        return f"__MASK{len(masks) - 1}__"

    # Mask path/filename-like tokens that contain bharatweld
    masked = re.sub(r"(?i)[\w./\\-]*bharatweld[\w./\\-]*", mask, text)

    masked = re.sub(r"\bBHARATWELD\b(?!\s*™)(?!&trade;)", "BHARATWELD™", masked)
    masked = re.sub(r"\bBharatweld\b(?!\s*™)(?!&trade;)", "BHARATWELD™", masked)
    masked = re.sub(r"\bbharatweld\b(?!\s*™)(?!&trade;)", "BHARATWELD™", masked)

    def unmask(m: re.Match[str]) -> str:
        val = masks[int(m.group(1))]
        if re.fullmatch(r"(?i)bharatweld", val):
            return "BHARATWELD™"
        return val

    out = re.sub(r"__MASK(\d+)__", unmask, masked)
    out = out.replace("BHARATWELD™™", "BHARATWELD™")
    out = out.replace("BHARATWELD™&trade;", "BHARATWELD™")
    out = out.replace("BHARATWELD&trade;", "BHARATWELD™")
    return out


def main() -> None:
    changed: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or should_skip(path):
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)).replace("\\", "/"))
    print(f"updated {len(changed)} files")
    for p in changed:
        print(p)


if __name__ == "__main__":
    main()
