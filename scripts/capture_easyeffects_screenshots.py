#!/usr/bin/env python3
"""Capture Easy Effects main window for each project preset."""
from __future__ import annotations

import os
import re
import subprocess
import time
from pathlib import Path

from PIL import Image

os.environ["DISPLAY"] = ":0"
ROOT = Path("/mnt/dados/DEV/easyeffects-presets-premium")
RAW = ROOT / "validation/screenshots/raw"
MAIN = ROOT / "validation/screenshots/main"
CHAIN = ROOT / "validation/screenshots/chain"
for d in (RAW, MAIN, CHAIN, ROOT / "screenshots"):
    d.mkdir(parents=True, exist_ok=True)

PRESETS = [
    "cinema-01",
    "cinema-02",
    "classic-music-01",
    "music-hd-01",
    "music-hd-02",
    "gaming-01",
    "gaming-02",
    "voice-boost-01",
    "voice-boost-02",
    "volume-booster-01",
    "fxsound-ultimate-02",
]


def run(cmd, timeout=None):
    return subprocess.run(
        cmd,
        timeout=timeout,
        env={**os.environ, "DISPLAY": ":0"},
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def show_window():
    # Activate existing instance / raise UI
    subprocess.Popen(
        ["flatpak", "run", "com.github.wwmm.easyeffects"],
        env={**os.environ, "DISPLAY": ":0"},
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1.5)
    run(["wmctrl", "-a", "Easy Effects"], timeout=3)


def find_wid() -> str | None:
    out = subprocess.check_output(
        ["xwininfo", "-root", "-tree"],
        env={**os.environ, "DISPLAY": ":0"},
        text=True,
    )
    # Prefer the large mapped Easy Effects window
    pattern = re.compile(
        r'^\s+(0x[0-9a-f]+)\s+"Easy Effects":\s+\("easyeffects"\s+"easyeffects"\)\s+(\d+)x(\d+)',
        re.M,
    )
    best = None
    for m in pattern.finditer(out):
        wid, w, h = m.group(1), int(m.group(2)), int(m.group(3))
        if w >= 800 and h >= 600:
            best = wid
    return best


def load_preset(name: str):
    try:
        run(["flatpak", "run", "com.github.wwmm.easyeffects", "-l", name], timeout=5)
    except subprocess.TimeoutExpired:
        pass


def capture(path: Path) -> str:
    wid = None
    for _ in range(8):
        show_window()
        wid = find_wid()
        if wid:
            break
        time.sleep(0.5)
    if not wid:
        raise RuntimeError("Easy Effects window not found")
    run(["wmctrl", "-i", "-a", wid], timeout=3)
    time.sleep(0.4)
    subprocess.run(
        ["import", "-window", wid, str(path)],
        check=True,
        env={**os.environ, "DISPLAY": ":0"},
    )
    return wid


def main():
    show_window()
    results = []
    for p in PRESETS:
        print(f"loading {p}", flush=True)
        load_preset(p)
        time.sleep(0.8)
        dest = RAW / f"{p}-main.png"
        try:
            wid = capture(dest)
            img = Image.open(dest)
            img.save(MAIN / f"{p}.png")
            img.save(CHAIN / f"{p}.png")
            img.save(ROOT / "screenshots" / f"{p}.png")
            print(f"OK {p} {img.size} wid={wid}", flush=True)
            results.append(p)
        except Exception as e:
            print(f"FAIL {p}: {e}", flush=True)

    if (MAIN / "cinema-01.png").exists():
        Image.open(MAIN / "cinema-01.png").save(ROOT / "screenshots" / "overview.png")
    print(f"captured {len(results)}/{len(PRESETS)}", flush=True)


if __name__ == "__main__":
    main()
