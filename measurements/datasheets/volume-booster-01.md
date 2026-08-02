# Datasheet: `volume-booster-01`

| Field | Value |
|-------|-------|
| Category | experimental |
| File | `presets/experimental/volume-booster-01.json` |
| Objective | Raise perceived loudness safely on quiet devices |
| Recommended hardware | Notebook speakers; quiet HP amps |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`equalizer#0 → compressor#0 → limiter#0`

- **Equalizer** (IIR, bands=10): tonal core. See curve table.
- **Compressor**: thr=-18.0 dB, ratio=2.5, attack=10.0 ms, release=80.0 ms, makeup=6.0 dB.
- **Limiter**: ceiling/limit=-0.5, lookahead=5.0, release=40.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 32 | +2.0 |
| 64 | +2.0 |
| 125 | +2.0 |
| 250 | +2.0 |
| 500 | +2.0 |
| 1000 | +2.0 |
| 2000 | +2.0 |
| 4000 | +2.0 |
| 8000 | +2.0 |
| 16000 | +2.0 |

## Expected result

Higher loudness vs Flat with limiter safety

## Limitations

Flat +2 dB shelf is crude; can clip soft encodes before limiter if mis-set

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 3.0 |
| Bass Control | 3.0 |
| Treble Detail | 3.0 |
| Stereo Width | 2.5 |
| Dynamic Control | 3.0 |
| Listening Fatigue | 2.5 |
| Perceived Loudness | 4.5 |
| Gaming Positioning | 2.0 |
| Movie Immersion | 2.5 |
| Music Fidelity | 2.5 |

**Primary weights for category:** Perceived Loudness, Bass Control

## Engineering notes

- `*-01` / simple chains kept topology stable in FASE 03; parameters already category-specific.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

