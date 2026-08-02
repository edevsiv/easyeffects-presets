# Audio profile — `volume-booster-01`

| Field | Value |
|-------|-------|
| ID | `volume-booster-01` |
| Category | experimental |
| Objective | Simple loudness shelf boost |
| Version | aligned with `v1.0.0-rc1` artifact set |
| Seal | **Beta** |
| License | MIT (repository) |
| Preset JSON | [`presets/experimental/volume-booster-01.json`](../../presets/experimental/volume-booster-01.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `notebook` |
| Validated (evidence) | `HW-001` (UI/screenshots; listening pending) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `equalizer`, `limiter` |
| Pipeline | `Equalizer → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/volume-booster-01.md](../../measurements/datasheets/volume-booster-01.md) |
| Validation dossier | [validation/profiles/volume-booster-01.md](../../validation/profiles/volume-booster-01.md) |
| Limitations | Crude flat boost |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Validated seal requires listening forms.
