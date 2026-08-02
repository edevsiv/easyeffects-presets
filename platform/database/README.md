# Platform databases

Canonical schemas and indexes for the Audio Platform.

| Database | Schema | Index |
|----------|--------|-------|
| Audio profiles | [SCHEMA_PROFILES.md](SCHEMA_PROFILES.md) | [profiles.json](profiles.json) · [index.md](index.md) |
| Hardware | [../hardware/SCHEMA.md](../hardware/SCHEMA.md) | [../hardware/](../hardware/) |
| Calibration | [../calibration/README.md](../calibration/README.md) | links into `calibration/` |
| Impulse responses | [../../impulse-responses/catalog/SCORECARD.md](../../impulse-responses/catalog/SCORECARD.md) | catalog |

**Authority:** Markdown cards are human-facing; `profiles.json` is the machine index.
JSON presets remain the DSP source of truth under `presets/`.
