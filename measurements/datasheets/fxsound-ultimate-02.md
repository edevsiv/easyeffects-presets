# Datasheet: `fxsound-ultimate-02`

| Field | Value |
|-------|-------|
| Category | experimental |
| File | `presets/experimental/fxsound-ultimate-02.json` |
| Objective | FxSound-inspired wide/exciting enhancer chain |
| Recommended hardware | Notebook speakers (primary migrant case) |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`autogain#0 → multiband_compressor#0 → equalizer#0 → exciter#0 → bass_enhancer#0 → stereo_tools#0 → limiter#0`

- **Autogain**: target=-18 LUFS-ish, reference=Geometric Mean (MSI).
- **Multiband Compressor**: mode=Modern; density/loudness glue (inspect band enables in JSON).
- **Equalizer** (IIR, bands=32): tonal core. See curve table.
- **Exciter**: amount=18.0, harmonics=8.5, scope=7500.0 Hz.
- **Bass Enhancer**: amount=20.0, harmonics=8.5, scope=100.0, blend=30.0.
- **Stereo Tools**: stereo-base=12.0, side-level=0.0, mode=LR > LR (Stereo Default).
- **Limiter**: ceiling/limit=-0.8, lookahead=5.0, release=5.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 22.4 | +3.0 |
| 27.8 | +3.0 |
| 34.51 | +3.0 |
| 42.82 | +3.0 |
| 53.14 | +3.0 |
| 65.95 | +3.0 |
| 81.83 | +3.0 |
| 101.55 | +2.0 |
| 126 | +2.0 |
| 156.38 | +2.0 |
| 194.06 | +2.0 |
| 879.387 | +2.0 |
| 1091.26 | +2.0 |
| 1680.47 | +3.0 |

## Expected result

Wow-factor bass/clarity/width vs Flat

## Limitations

Fatigue risk; not fidelity; not Dolby virtualizer

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 3.0 |
| Bass Control | 4.0 |
| Treble Detail | 3.5 |
| Stereo Width | 4.0 |
| Dynamic Control | 3.5 |
| Listening Fatigue | 2.5 |
| Perceived Loudness | 4.5 |
| Gaming Positioning | 2.5 |
| Movie Immersion | 3.5 |
| Music Fidelity | 3.0 |

**Primary weights for category:** Perceived Loudness, Bass Control

## Engineering notes

- Shares historical DNA with the heavy Autogain→Multiband→Enhancer template; FASE 03 differentiated enhancer amounts by category.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

