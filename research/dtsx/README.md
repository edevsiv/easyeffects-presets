# Research: DTS:X / DTS Sound Unbound

**Sources:** [DTS Sound Unbound](https://consumer.dts.com/dts-sound-unbound/), DTS FAQ, Windows Spatial Sound docs.

## Summary

DTS Sound Unbound exposes **DTS Headphone:X** (headphones) and **DTS:X Ultra** (often OEM speakers) through Windows Spatial Sound. Focus is **object/spatial rendering**, headphone-specific tunings, and immersive gaming/movie modes.

## Features

| Feature | Notes |
|---------|-------|
| DTS Headphone:X | 3D spatial over any headphones; large headphone tuning DB (500+) |
| DTS:X Ultra | Speaker-oriented spatial + OEM tuning |
| Modes | Game / Entertainment / Traditional (varies by build) |
| Dialog / bass tools | Present in many OEM UIs as clarity & bass enhancers |
| EQ | User EQ + profile tunings |

## Strengths

- Competitive positional audio for games
- Headphone model database
- Deep Windows platform integration

## Limitations

- Windows Spatial Sound dependency
- Closed HRTF / object renderer
- Feature set varies wildly by OEM SKU / license

## EasyEffects equivalence

| DTS capability | EasyEffects | Notes |
|----------------|-------------|-------|
| Spatial / Headphone:X | Convolver + HRTF/SOFA packs | Community IRs; not DTS DB |
| Dialog clarity | Voice-oriented EQ/dynamics | Approximate |
| Bass | Bass Enhancer | Approximate |
| Low-latency game mode | Lighter plugin chains + PipeWire quantum | Operational, not algorithmic clone |

## Project stance

Treat DTS as the **spatial reference** we cannot legally/clone bit-identically. Invest in curated open HRTF packs under `impulse-responses/` (future) and honest stereo imaging via Stereo Tools for v1–v2 presets.
