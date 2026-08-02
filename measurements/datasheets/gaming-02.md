# Datasheet: `gaming-02`

| Field | Value |
|-------|-------|
| Category | gaming |
| File | `presets/gaming/gaming-02.json` |
| Objective | Immersive single-player presentation |
| Recommended hardware | Headset; higher quantum OK |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`autogain#0 → multiband_compressor#0 → equalizer#0 → exciter#0 → bass_enhancer#0 → stereo_tools#0 → limiter#0`

- **Autogain**: target=-19 LUFS-ish, reference=Geometric Mean (MSI).
- **Multiband Compressor**: mode=Modern; density/loudness glue (inspect band enables in JSON).
- **Equalizer** (IIR, bands=32): tonal core. See curve table.
- **Exciter**: amount=10.0, harmonics=8.5, scope=7500.0 Hz.
- **Bass Enhancer**: amount=10.0, harmonics=8.5, scope=100.0, blend=15.0.
- **Stereo Tools**: stereo-base=8.0, side-level=0.0, mode=LR > LR (Stereo Default).
- **Limiter**: ceiling/limit=-0.8, lookahead=5.0, release=5.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 53.14 | +1.0 |
| 65.95 | +1.0 |
| 81.83 | +1.0 |
| 101.55 | +1.0 |
| 126 | +1.0 |
| 156.38 | +1.0 |
| 194.06 | +1.0 |
| 1680.47 | +3.0 |
| 2085.35 | +3.0 |
| 3211.29 | +3.0 |
| 3985.01 | +3.0 |
| 6136.63 | +2.0 |
| 7615.17 | +2.0 |

## Expected result

Dense, exciting world audio with leveling

## Limitations

Positional purity < gaming-01; enhancer residue

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
| Gaming Positioning | 3.5 |
| Movie Immersion | 3.5 |
| Music Fidelity | 2.5 |

**Primary weights for category:** Gaming Positioning, Dynamic Control

## Engineering notes

- Shares historical DNA with the heavy Autogain→Multiband→Enhancer template; FASE 03 differentiated enhancer amounts by category.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

