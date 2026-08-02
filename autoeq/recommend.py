#!/usr/bin/env python3
"""Experimental AutoEQ recommendation generator.

Reads an Equalizer APO ParametricEQ.txt and emits Markdown recommendations.
Does NOT modify EasyEffects presets.
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path


def _load_parser():
    path = Path(__file__).with_name("convert_apo_to_bands.py")
    spec = importlib.util.spec_from_file_location("convert_apo_to_bands", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.parse


def recommend(preamp, bands, headphone: str, content_preset: str | None) -> str:
    lines = [
        f"# AutoEQ recommendation — `{headphone}`",
        "",
        "## Summary",
        "",
        "Apply headphone correction **before** or **instead of** stacking smile-curve content EQ.",
        "",
        f"- Suggested preamp: **{preamp if preamp is not None else 0.0} dB** (from APO file)",
        f"- Filters parsed: **{len(bands)}**",
        "",
        "## How to apply (manual)",
        "",
        "1. EasyEffects → Equalizer → **APO** → import the ParametricEQ.txt",
        "2. Confirm meters do not slam the limiter on quiet content",
        "3. Then load a content preset **or** use a future `no-eq` variant",
        "",
        "## Interaction warning",
        "",
    ]
    if content_preset:
        lines += [
            f"Requested content preset: `{content_preset}`",
            "",
            "If that preset already boosts bass/treble heavily (`music-hd-*`, `fxsound-*`, `*-02`),",
            "prefer Flat content EQ or reduce enhancer amounts after correction.",
            "",
        ]
    lines += [
        "## Band table",
        "",
        "| # | Type | Fc (Hz) | Gain (dB) | Q |",
        "|--:|------|--------:|----------:|----:|",
    ]
    for i, b in enumerate(bands, 1):
        lines.append(
            f"| {i} | {b['type']} | {b['fc']:.2f} | {b['gain']:+.2f} | {b['q']:.2f} |"
        )
    lines += [
        "",
        "## Validation",
        "",
        "Run listening form after applying; do not change seal without CERTIFICATION gates.",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("apo_file", type=Path)
    ap.add_argument("--headphone", required=True)
    ap.add_argument("--content-preset")
    ap.add_argument("-o", "--output", type=Path)
    args = ap.parse_args()
    parse = _load_parser()
    preamp, bands = parse(args.apo_file.read_text(encoding="utf-8", errors="replace"))
    md = recommend(preamp, bands, args.headphone, args.content_preset)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(md + "\n", encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(md)


if __name__ == "__main__":
    main()
