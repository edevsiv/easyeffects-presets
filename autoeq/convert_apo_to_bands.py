#!/usr/bin/env python3
"""Experimental: parse Equalizer APO ParametricEQ.txt into a band table.

Does NOT write EasyEffects JSON presets automatically.
Use EasyEffects Equalizer → APO import for production loading.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

FILTER_RE = re.compile(
    r"^Filter\s+\d+:\s+ON\s+(?P<type>\w+)\s+Fc\s+(?P<fc>[0-9.]+)\s+Hz\s+Gain\s+(?P<gain>[-0-9.]+)\s+dB(?:\s+Q\s+(?P<q>[0-9.]+))?",
    re.I,
)
PREAMP_RE = re.compile(r"^Preamp:\s+([-0-9.]+)\s+dB", re.I)


def parse(text: str):
    preamp = None
    bands = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = PREAMP_RE.match(line)
        if m:
            preamp = float(m.group(1))
            continue
        m = FILTER_RE.match(line)
        if m:
            bands.append(
                {
                    "type": m.group("type"),
                    "fc": float(m.group("fc")),
                    "gain": float(m.group("gain")),
                    "q": float(m.group("q") or 1.0),
                }
            )
    return preamp, bands


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("apo_file", type=Path)
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args()
    preamp, bands = parse(args.apo_file.read_text(encoding="utf-8", errors="replace"))
    if args.markdown:
        print(f"# APO parse — `{args.apo_file.name}`\n")
        print(f"Preamp: **{preamp} dB**\n" if preamp is not None else "Preamp: _(none)_\n")
        print("| # | Type | Fc (Hz) | Gain (dB) | Q |")
        print("|--:|------|--------:|----------:|----:|")
        for i, b in enumerate(bands, 1):
            print(f"| {i} | {b['type']} | {b['fc']:.2f} | {b['gain']:+.2f} | {b['q']:.2f} |")
        print("\nNext: EasyEffects → Equalizer → **APO** → select this file.")
    else:
        print({"preamp": preamp, "bands": bands})


if __name__ == "__main__":
    main()
