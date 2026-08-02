# Datasheet: `gaming-01`

| Field | Value |
|-------|-------|
| Category | gaming |
| File | `presets/gaming/gaming-01.json` |
| Objective | Competitive clarity and controlled punch |
| Recommended hardware | Gaming headset; low quantum preferred |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`equalizer#0 → bass_enhancer#0 → stereo_tools#0 → compressor#0 → limiter#0`

- **Equalizer** (IIR, bands=10): tonal core. See curve table.
- **Bass Enhancer**: amount=5.0, harmonics=6.0, scope=Mono, blend=0.25.
- **Stereo Tools**: stereo-base=0.25, side-level=1.1, mode=LR > LR (Stereo Default).
- **Compressor**: thr=-20.0 dB, ratio=2.5, attack=6.0 ms, release=90.0 ms, makeup=3.0 dB.
- **Limiter**: ceiling/limit=-1.0, lookahead=5.0, release=40.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 32 | +4.0 |
| 64 | +3.0 |
| 125 | +1.0 |
| 500 | -1.0 |
| 1000 | +0.5 |
| 2000 | +2.5 |
| 4000 | +4.5 |
| 8000 | +5.0 |
| 16000 | +3.5 |

## Expected result

Footstep/presence emphasis; controlled explosions

## Limitations

Not immersive cinema; bright EQ may fatigue long sessions

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 3.5 |
| Bass Control | 3.0 |
| Treble Detail | 4.0 |
| Stereo Width | 3.5 |
| Dynamic Control | 3.5 |
| Listening Fatigue | 3.5 |
| Perceived Loudness | 3.0 |
| Gaming Positioning | 4.5 |
| Movie Immersion | 2.5 |
| Music Fidelity | 2.5 |

**Primary weights for category:** Gaming Positioning, Dynamic Control

## Engineering notes

- `*-01` / simple chains kept topology stable in FASE 03; parameters already category-specific.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

