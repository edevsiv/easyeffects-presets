#!/usr/bin/env python3
"""Capture EQ and compressor/multiband views for each preset."""
from __future__ import annotations

import os
import re
import subprocess
import time
from pathlib import Path

from Xlib import X, display
from Xlib.ext import xtest

os.environ["DISPLAY"] = ":0"
ROOT = Path("/mnt/dados/DEV/easyeffects-presets-premium")
RAW = ROOT / "validation/screenshots/raw"
EQD = ROOT / "validation/screenshots/equalizer"
COMPD = ROOT / "validation/screenshots/compressor"
for d in (RAW, EQD, COMPD):
    d.mkdir(parents=True, exist_ok=True)

ORDERS = {
    "cinema-01": ["equalizer", "bass_enhancer", "compressor", "limiter"],
    "cinema-02": [
        "autogain",
        "multiband_compressor",
        "equalizer",
        "exciter",
        "bass_enhancer",
        "stereo_tools",
        "limiter",
    ],
    "classic-music-01": ["equalizer", "reverb", "limiter"],
    "music-hd-01": ["equalizer", "exciter", "stereo_tools", "limiter"],
    "music-hd-02": [
        "autogain",
        "multiband_compressor",
        "equalizer",
        "exciter",
        "bass_enhancer",
        "stereo_tools",
        "limiter",
    ],
    "gaming-01": ["equalizer", "bass_enhancer", "stereo_tools", "compressor", "limiter"],
    "gaming-02": [
        "autogain",
        "multiband_compressor",
        "equalizer",
        "exciter",
        "bass_enhancer",
        "stereo_tools",
        "limiter",
    ],
    "voice-boost-01": ["equalizer", "gate", "compressor", "deesser", "limiter"],
    "voice-boost-02": [
        "autogain",
        "multiband_compressor",
        "equalizer",
        "exciter",
        "bass_enhancer",
        "stereo_tools",
        "limiter",
    ],
    "volume-booster-01": ["equalizer", "compressor", "limiter"],
    "fxsound-ultimate-02": [
        "autogain",
        "multiband_compressor",
        "equalizer",
        "exciter",
        "bass_enhancer",
        "stereo_tools",
        "limiter",
    ],
}


def run(cmd, timeout=None):
    return subprocess.run(
        cmd,
        timeout=timeout,
        env={**os.environ, "DISPLAY": ":0"},
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def show_window():
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
    pat = re.compile(
        r'^\s+(0x[0-9a-f]+)\s+"Easy Effects":\s+\("easyeffects"\s+"easyeffects"\)\s+(\d+)x(\d+)',
        re.M,
    )
    best = None
    for m in pat.finditer(out):
        if int(m.group(2)) >= 800 and int(m.group(3)) >= 600:
            best = m.group(1)
    return best


def wait_wid(retries: int = 12) -> str:
    for _ in range(retries):
        show_window()
        wid = find_wid()
        if wid:
            return wid
        time.sleep(0.4)
    raise RuntimeError("Easy Effects window not found")


def window_abs(wid_hex: str):
    out = subprocess.check_output(
        ["xwininfo", "-id", wid_hex],
        env={**os.environ, "DISPLAY": ":0"},
        text=True,
    )
    x = y = w = h = 0
    for line in out.splitlines():
        if "Absolute upper-left X" in line:
            x = int(line.split()[-1])
        elif "Absolute upper-left Y" in line:
            y = int(line.split()[-1])
        elif line.strip().startswith("Width:"):
            w = int(line.split()[-1])
        elif line.strip().startswith("Height:"):
            h = int(line.split()[-1])
    return x, y, w, h


def load_preset(name: str):
    try:
        run(["flatpak", "run", "com.github.wwmm.easyeffects", "-l", name], timeout=5)
    except subprocess.TimeoutExpired:
        pass


def click(abs_x: int, abs_y: int):
    d = display.Display()
    xtest.fake_input(d, X.MotionNotify, x=int(abs_x), y=int(abs_y))
    d.sync()
    time.sleep(0.05)
    xtest.fake_input(d, X.ButtonPress, 1)
    d.sync()
    xtest.fake_input(d, X.ButtonRelease, 1)
    d.sync()


def capture(path: Path, wid: str):
    run(["wmctrl", "-i", "-a", wid], timeout=3)
    time.sleep(0.35)
    subprocess.run(
        ["import", "-window", wid, str(path)],
        check=True,
        env={**os.environ, "DISPLAY": ":0"},
    )


def click_plugin(wid: str, index: int):
    x, y, w, h = window_abs(wid)
    cx = x + 130
    cy = y + 200 + index * 70
    click(cx, cy)
    time.sleep(0.7)


def plugin_index(order: list[str], kind: str) -> int | None:
    for i, name in enumerate(order):
        if kind == "equalizer" and name.startswith("equalizer"):
            return i
        if kind == "compressor" and name in ("compressor", "multiband_compressor"):
            return i
    return None


def main():
    for preset, order in ORDERS.items():
        print(f"=== {preset}", flush=True)
        load_preset(preset)
        time.sleep(0.6)
        wid = wait_wid()

        eq_i = plugin_index(order, "equalizer")
        if eq_i is not None:
            click_plugin(wid, eq_i)
            path = EQD / f"{preset}.png"
            capture(path, wid)
            capture(RAW / f"{preset}-equalizer.png", wid)
            print(f"  EQ idx={eq_i} -> {path}", flush=True)

        comp_i = plugin_index(order, "compressor")
        if comp_i is not None:
            click_plugin(wid, comp_i)
            path = COMPD / f"{preset}.png"
            capture(path, wid)
            capture(RAW / f"{preset}-compressor.png", wid)
            print(f"  COMP idx={comp_i} -> {path}", flush=True)
        else:
            print("  no compressor/multiband", flush=True)

    print("done", flush=True)


if __name__ == "__main__":
    main()
