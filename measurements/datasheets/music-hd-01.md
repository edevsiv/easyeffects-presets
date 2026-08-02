# Datasheet: `music-hd-01`

| Field | Value |
|-------|-------|
| Category | music |
| File | `presets/music/music-hd-01.json` |
| Objective | Clean music clarity with tasteful excitement and width |
| Recommended hardware | Headphones/IEM; USB DAC preferred |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`equalizer#0 → exciter#0 → stereo_tools#0 → limiter#0`

- **Equalizer** (IIR, bands=10): tonal core. See curve table.
- **Exciter**: amount=4.0, harmonics=6.0, scope=7500.0 Hz.
- **Stereo Tools**: stereo-base=0.15, side-level=1.05, mode=LR > LR (Stereo Default).
- **Limiter**: ceiling/limit=-1.0, lookahead=5.0, release=50.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 32 | +3.0 |
| 64 | +2.0 |
| 250 | -1.0 |
| 500 | -1.0 |
| 2000 | +1.0 |
| 4000 | +2.0 |
| 8000 | +3.0 |
| 16000 | +3.0 |

## Expected result

More air and slight width vs Flat without loudness war

## Limitations

Not headphone-corrected (no AutoEQ yet)

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 3.0 |
| Bass Control | 3.5 |
| Treble Detail | 4.0 |
| Stereo Width | 3.5 |
| Dynamic Control | 3.5 |
| Listening Fatigue | 4.0 |
| Perceived Loudness | 3.0 |
| Gaming Positioning | 2.5 |
| Movie Immersion | 2.5 |
| Music Fidelity | 4.0 |

**Primary weights for category:** Music Fidelity, Treble Detail, Bass Control

## Engineering notes

- `*-01` / simple chains kept topology stable in FASE 03; parameters already category-specific.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

