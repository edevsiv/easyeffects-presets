# Datasheet: `cinema-02`

| Field | Value |
|-------|-------|
| Category | movie |
| File | `presets/movie/cinema-02.json` |
| Objective | Leveled immersive cinema for inconsistent streaming loudness |
| Recommended hardware | Headphones; notebook; avoid stacking OEM Dolby |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`autogain#0 → multiband_compressor#0 → equalizer#0 → exciter#0 → bass_enhancer#0 → stereo_tools#0 → limiter#0`

- **Autogain**: target=-18 LUFS-ish, reference=Geometric Mean (MSI).
- **Multiband Compressor**: mode=Modern; density/loudness glue (inspect band enables in JSON).
- **Equalizer** (IIR, bands=32): tonal core. See curve table.
- **Exciter**: amount=18.0, harmonics=8.5, scope=7500.0 Hz.
- **Bass Enhancer**: amount=14.0, harmonics=8.5, scope=100.0, blend=20.0.
- **Stereo Tools**: stereo-base=10.0, side-level=0.0, mode=LR > LR (Stereo Default).
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
| 879.387 | +1.0 |
| 1091.26 | +1.0 |
| 1680.47 | +3.0 |

## Expected result

More consistent loudness; denser immersion; watch center dialog

## Limitations

Heavy enhancers; not critical music; needs A/B confirmation post-trim

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 3.5 |
| Bass Control | 3.5 |
| Treble Detail | 3.5 |
| Stereo Width | 3.5 |
| Dynamic Control | 4.0 |
| Listening Fatigue | 3.0 |
| Perceived Loudness | 4.0 |
| Gaming Positioning | 2.5 |
| Movie Immersion | 4.0 |
| Music Fidelity | 2.5 |

**Primary weights for category:** Voice Clarity, Movie Immersion, Dynamic Control

## Engineering notes

- Shares historical DNA with the heavy Autogain→Multiband→Enhancer template; FASE 03 differentiated enhancer amounts by category.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

