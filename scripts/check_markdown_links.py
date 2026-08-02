#!/usr/bin/env python3
"""Basic Markdown relative-link checker for repository docs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def iter_markdown() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    errors = 0
    checked = 0
    for md in iter_markdown():
        text = md.read_text(encoding="utf-8")
        for _label, target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith(SKIP_PREFIXES):
                continue
            # strip anchors
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            checked += 1
            resolved = (md.parent / path_part).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                print(f"OUTSIDE REPO: {md.relative_to(ROOT)} -> {target}")
                errors += 1
                continue
            if not resolved.exists():
                print(f"BROKEN: {md.relative_to(ROOT)} -> {target}")
                errors += 1

    if errors:
        print(f"Markdown link check failed ({errors} broken, {checked} relative links).")
        return 1
    print(f"Markdown link check passed ({checked} relative links).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
