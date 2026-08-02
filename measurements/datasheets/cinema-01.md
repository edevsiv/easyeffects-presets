# Datasheet: `cinema-01`

| Field | Value |
|-------|-------|
| Category | movie |
| File | `presets/movie/cinema-01.json` |
| Objective | Balanced cinematic playback with dialog presence and controlled bass |
| Recommended hardware | Headphones P0; notebook speakers P0 |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`equalizer#0 → bass_enhancer#0 → compressor#0 → limiter#0`

- **Equalizer** (IIR, bands=10): tonal core. See curve table.
- **Bass Enhancer**: amount=6.0, harmonics=8.0, scope=Mono, blend=0.3.
- **Compressor**: thr=-22.0 dB, ratio=3.0, attack=15.0 ms, release=150.0 ms, makeup=2.0 dB.
- **Limiter**: ceiling/limit=-1.0, lookahead=5.0, release=60.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 32 | +4.0 |
| 64 | +3.0 |
| 125 | +1.0 |
| 500 | +1.5 |
| 1000 | +2.5 |
| 2000 | +3.0 |
| 4000 | +2.0 |
| 8000 | +1.0 |

## Expected result

Clearer dialog than Flat; moderate LFE; low fatigue

## Limitations

Not a night-mode DRC; weak on highly dynamic Blu-ray without autogain

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 4.0 |
| Bass Control | 3.5 |
| Treble Detail | 3.5 |
| Stereo Width | 3.0 |
| Dynamic Control | 3.5 |
| Listening Fatigue | 4.0 |
| Perceived Loudness | 3.0 |
| Gaming Positioning | 2.5 |
| Movie Immersion | 4.0 |
| Music Fidelity | 3.0 |

**Primary weights for category:** Voice Clarity, Movie Immersion, Dynamic Control

## Engineering notes

- `*-01` / simple chains kept topology stable in FASE 03; parameters already category-specific.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

