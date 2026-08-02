# Datasheet: `music-hd-02`

| Field | Value |
|-------|-------|
| Category | music |
| File | `presets/music/music-hd-02.json` |
| Objective | Commercial enhanced music listening |
| Recommended hardware | Notebook speakers; casual headphones |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`autogain#0 → multiband_compressor#0 → equalizer#0 → exciter#0 → bass_enhancer#0 → stereo_tools#0 → limiter#0`

- **Autogain**: target=-20 LUFS-ish, reference=Geometric Mean (MSI).
- **Multiband Compressor**: mode=Modern; density/loudness glue (inspect band enables in JSON).
- **Equalizer** (IIR, bands=32): tonal core. See curve table.
- **Exciter**: amount=10.0, harmonics=8.5, scope=7500.0 Hz.
- **Bass Enhancer**: amount=12.0, harmonics=8.5, scope=100.0, blend=18.0.
- **Stereo Tools**: stereo-base=8.0, side-level=0.0, mode=LR > LR (Stereo Default).
- **Limiter**: ceiling/limit=-0.8, lookahead=5.0, release=5.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 22.4 | +2.0 |
| 27.8 | +2.0 |
| 34.51 | +2.0 |
| 42.82 | +2.0 |
| 53.14 | +2.0 |
| 65.95 | +2.0 |
| 81.83 | +2.0 |
| 101.55 | +3.0 |
| 126 | +3.0 |
| 156.38 | +3.0 |
| 194.06 | +3.0 |
| 3985.01 | +2.0 |
| 4945.15 | +2.0 |
| 7615.17 | +2.0 |

## Expected result

Louder, denser playlist presentation

## Limitations

Can fatigue on bright IEMs; not fidelity-first

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 3.0 |
| Bass Control | 3.5 |
| Treble Detail | 3.5 |
| Stereo Width | 3.5 |
| Dynamic Control | 3.5 |
| Listening Fatigue | 3.0 |
| Perceived Loudness | 4.0 |
| Gaming Positioning | 2.0 |
| Movie Immersion | 2.5 |
| Music Fidelity | 3.5 |

**Primary weights for category:** Music Fidelity, Treble Detail, Bass Control

## Engineering notes

- Shares historical DNA with the heavy Autogain→Multiband→Enhancer template; FASE 03 differentiated enhancer amounts by category.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

