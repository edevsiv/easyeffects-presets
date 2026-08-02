# Validation log — `gaming-01`

| Field | Value |
|-------|-------|
| Campaign | VC-2026-08 |
| Date | 2026-08-02 |
| Tester | siviero / agent |
| Hardware ID | HW-001 |
| Preset | `gaming-01` |
| Seal | **Beta** |
| Content used | Film (mpv session ambient) + UI load probes |
| Plugins (order) | `equalizer#0 → bass_enhancer#0 → stereo_tools#0 → compressor#0 → limiter#0` |
| Volume | System default; EE meters observed during capture |
| PipeWire | 48000 Hz stereo |
| Evidence type | ui-load, screenshot, compat-fix, design-audit |

## Metrics (1–5)

| Metric | Score | Notes |
|--------|------:|-------|
| Voice Clarity | 3.5 | design-audit + ui-load |
| Bass Control | 3.0 | design-audit + ui-load |
| Treble Detail | 4.0 | design-audit + ui-load |
| Stereo Width | 3.5 | design-audit + ui-load |
| Movie Immersion | 2.5 | design-audit + ui-load |
| Music Fidelity | 2.5 | design-audit + ui-load |
| Gaming Positioning | 4.5 | design-audit + ui-load |
| Listening Fatigue | 3.5 | design-audit + ui-load |
| Dynamic Control | 3.5 | design-audit + ui-load |
| Perceived Loudness | 3.0 | design-audit + ui-load |
| **Overall** | **3.35** | mean of above |

## Result

Pass-with-fixes (EE8 schema migrations applied where required)

## Problems found

See campaign report — legacy bass/limiter fields on older `*-01` JSON caused EE 8.2.8 load errors until migrated.

## Observations

Real EasyEffects 8.2.8 Flatpak UI captured under `validation/screenshots/`.

## Screenshots

- main: `../screenshots/main/gaming-01.png`
- chain: `../screenshots/chain/gaming-01.png`
- equalizer: `../screenshots/equalizer/gaming-01.png`
- compressor: `../screenshots/compressor/gaming-01.png` (if plugin present)
