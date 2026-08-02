# Measurements laboratory

Scientific validation home for EasyEffects Presets Premium.

| Path | Purpose |
|------|---------|
| [METRICS.md](METRICS.md) | Official metric definitions + scales |
| [TEST_MATRIX.md](TEST_MATRIX.md) | All-preset technical matrix |
| [datasheets/](datasheets/) | Per-preset technical sheets |
| [version-history/](version-history/) | Why/what/expected per change |
| [subjective/](subjective/) | Listening + A/B logs |
| [objective/](objective/) | Meter / RTA notes |
| [device-tests/](device-tests/) | Device × preset sessions |
| [hardware/](hardware/) | Hardware bank |
| [reference-results/](reference-results/) | Frozen release scorecards |
| [ENGINEERING_REVIEW_FASE03.md](ENGINEERING_REVIEW_FASE03.md) | FASE 03 audit |
| [LOG_TEMPLATE.md](LOG_TEMPLATE.md) | Generic session log |

## Evidence ladder

1. `design-audit` — parameter analysis (done for all presets in FASE 03)
2. `ab-test` — old vs new (+ Flat / FxSound / Dolby when relevant)
3. `subjective-log` — full metric scores on known hardware
4. `objective-measure` — LUFS / peaks / spectrum notes

No JSON merge without climbing at least to step 2 for DSP changes.
