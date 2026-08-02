# Datasheet: `voice-boost-01`

| Field | Value |
|-------|-------|
| Category | voice |
| File | `presets/voice/voice-boost-01.json` |
| Objective | Speech intelligibility for podcasts and talks |
| Recommended hardware | Any; headphones preferred |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`equalizer#0 → gate#0 → compressor#0 → deesser#0 → limiter#0`

- **Equalizer** (IIR, bands=10): tonal core. See curve table.
- **Gate**: thr=-45.0, attack=10.0, release=150.0, reduction=-40.0.
- **Compressor**: thr=-20.0 dB, ratio=3.5, attack=8.0 ms, release=120.0 ms, makeup=4.0 dB.
- **De-esser**: f1=5500.0, f2=8500.0, ratio=3.5, mode=Wide.
- **Limiter**: ceiling/limit=-1.0, lookahead=5.0, release=50.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 32 | -4.0 |
| 64 | -3.0 |
| 125 | -1.0 |
| 250 | +2.0 |
| 500 | +4.5 |
| 1000 | +5.0 |
| 2000 | +4.0 |
| 4000 | +2.0 |
| 16000 | -2.0 |

## Expected result

Forward midrange speech; controlled sibilance

## Limitations

Output-only; not a mic chain; music beds may thin

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 4.5 |
| Bass Control | 2.5 |
| Treble Detail | 3.5 |
| Stereo Width | 2.5 |
| Dynamic Control | 4.0 |
| Listening Fatigue | 4.0 |
| Perceived Loudness | 3.5 |
| Gaming Positioning | 2.0 |
| Movie Immersion | 3.5 |
| Music Fidelity | 2.0 |

**Primary weights for category:** Voice Clarity, Listening Fatigue

## Engineering notes

- `*-01` / simple chains kept topology stable in FASE 03; parameters already category-specific.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

