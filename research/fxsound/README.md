# Research: FxSound

**Sources:** [fxsound2/fxsound-app](https://github.com/fxsound2/fxsound-app), [fxsound.com](https://www.fxsound.com/), DeepWiki audio pipeline docs.

## Summary

FxSound is an open-source Windows audio enhancer. It installs a **virtual audio driver**, captures system playback, processes audio in a high-priority thread via the **DfxDsp** engine, and plays the result to the physical device.

## Architecture

```text
Apps → FxSound Virtual Device → Audio Passthrough → DfxDsp → Physical Output
```

Components:

1. **GUI** (JUCE) — presets, EQ, effect sliders
2. **audiopassthru** — WASAPI device I/O, buffer/thread management
3. **DfxDsp** — real-time enhancement DSP

## DSP feature set

| Effect | Role | Typical range |
|--------|------|---------------|
| **Fidelity** | Clarity / high-frequency presence | 0–1 intensity |
| **Ambience** | Spatial / reverb-like space | 0–1 |
| **Surround** | Stage width / surround impression | 0–1 |
| **Dynamic Boost** | Perceived loudness + dynamic control | 0–1 |
| **Bass** | Low-frequency enhancement | 0–1 |
| **Equalizer** | Multi-band tonal shaping | per-band boost/cut |

Presets are stored as `.fac` files (FxSound format), not EasyEffects JSON.

## Strengths

- Extremely approachable UX for non-engineers
- Effective on **quiet laptop speakers**
- Open source → inspectable architecture
- Strong “wow” factor for migrants from stock Windows audio

## Limitations

- Windows-centric (virtual driver model)
- Proprietary-feeling “one knob” effects hide parameters
- Easy to over-process (fatigue, pumping)
- Not a substitute for room/headphone correction (AutoEQ)

## EasyEffects equivalence

| FxSound | EasyEffects mapping |
|---------|---------------------|
| Fidelity | `exciter` + high shelves / Crystalizer |
| Ambience | `reverb` (subtle) or `convolver` IR |
| Surround | `stereo_tools` (width, side) |
| Dynamic Boost | `autogain` + `compressor`/`multiband_compressor` + `limiter` |
| Bass | `bass_enhancer` |
| EQ | `equalizer` |

Project preset inspired by this stack: [`fxsound-ultimate-02`](../../presets/experimental/fxsound-ultimate-02.json).

## Recommended research next steps

1. Read DfxDsp sources for effect order and gain staging.
2. A/B FxSound “Cinema” / “Music” vs EasyEffects experimental presets on identical files.
3. Document knob→parameter translation tables for contributors.
