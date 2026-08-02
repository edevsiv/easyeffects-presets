# Datasheet: `classic-music-01`

| Field | Value |
|-------|-------|
| Category | music |
| File | `presets/music/classic-music-01.json` |
| Objective | Preserve dynamics with gentle tone and subtle space |
| Recommended hardware | Neutral headphones; USB DAC |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`equalizer#0 → reverb#0 → limiter#0`

- **Equalizer** (IIR, bands=10): tonal core. See curve table.
- **Reverb**: room=Large, decay=1.8, wet=-22.0, amount=-22.0.
- **Limiter**: ceiling/limit=-1.5, lookahead=5.0, release=100.0, gain-boost=False.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 32 | +1.0 |
| 64 | +1.0 |
| 4000 | +1.0 |
| 8000 | +1.0 |
| 16000 | +2.0 |

## Expected result

Slight sweetness/space without compression signature

## Limitations

Reverb may annoy purists; very light EQ only

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 3.0 |
| Bass Control | 3.0 |
| Treble Detail | 3.5 |
| Stereo Width | 3.0 |
| Dynamic Control | 4.5 |
| Listening Fatigue | 4.5 |
| Perceived Loudness | 2.5 |
| Gaming Positioning | 1.5 |
| Movie Immersion | 2.5 |
| Music Fidelity | 4.5 |

**Primary weights for category:** Music Fidelity, Treble Detail, Bass Control

## Engineering notes

- `*-01` / simple chains kept topology stable in FASE 03; parameters already category-specific.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

