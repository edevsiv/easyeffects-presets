# Datasheet: `voice-boost-02`

| Field | Value |
|-------|-------|
| Category | voice |
| File | `presets/voice/voice-boost-02.json` |
| Objective | Stronger leveling for mixed speech + music beds |
| Recommended hardware | Notebook; headphones |
| Evidence (current) | design-audit (FASE 03) |
| Last engineering pass | 2026-08-02 |

## Plugins / chain

`autogain#0 → multiband_compressor#0 → equalizer#0 → exciter#0 → bass_enhancer#0 → stereo_tools#0 → limiter#0`

- **Autogain**: target=-21 LUFS-ish, reference=Geometric Mean (MSI).
- **Multiband Compressor**: mode=Modern; density/loudness glue (inspect band enables in JSON).
- **Equalizer** (IIR, bands=32): tonal core. See curve table.
- **Exciter**: amount=8.0, harmonics=6.5, scope=7500.0 Hz.
- **Bass Enhancer**: amount=6.0, harmonics=6.5, scope=100.0, blend=10.0.
- **Stereo Tools**: stereo-base=5.0, side-level=0.0, mode=LR > LR (Stereo Default).
- **Limiter**: ceiling/limit=-0.8, lookahead=5.0, release=5.0, gain-boost=True.

## Equalizer curve (notable bands)

| Hz | Gain (dB) |
|----:|----------:|
| 879.387 | +2.0 |
| 1091.26 | +2.0 |
| 1680.47 | +4.0 |
| 2085.35 | +4.0 |
| 3211.29 | +4.0 |
| 3985.01 | +3.0 |

## Expected result

More consistent loudness than voice-01 with safer enhancers after FASE03

## Limitations

Not a true broadcast voice processor; still hybrid content chain

## Metric scorecard (design-audit)

| Metric | Score |
|--------|------:|
| Voice Clarity | 4.0 |
| Bass Control | 3.0 |
| Treble Detail | 3.5 |
| Stereo Width | 3.0 |
| Dynamic Control | 4.0 |
| Listening Fatigue | 3.5 |
| Perceived Loudness | 4.0 |
| Gaming Positioning | 2.0 |
| Movie Immersion | 3.0 |
| Music Fidelity | 2.5 |

**Primary weights for category:** Voice Clarity, Listening Fatigue

## Engineering notes

- Shares historical DNA with the heavy Autogain→Multiband→Enhancer template; FASE 03 differentiated enhancer amounts by category.
- Any future JSON change must add `measurements/version-history/` entry + A/B log.

