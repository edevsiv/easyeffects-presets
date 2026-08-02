# Audio profile — `cinema-01`

| Field | Value |
|-------|-------|
| ID | `cinema-01` |
| Category | movie |
| Objective | Clear dialogue and balanced cinema on laptop/desktop speakers |
| Version | aligned with `v1.0.0` artifact set |
| Seal | **Stable** |
| License | MIT (repository) |
| Preset JSON | [`presets/movie/cinema-01.json`](../../presets/movie/cinema-01.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `notebook`, `speakers-2.0`, `speakers-2.1` |
| Validated (evidence) | `HW-001` (UI + VC-2026-08-LISTEN) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `equalizer`, `bass_enhancer`, `stereo_tools`, `limiter` |
| Pipeline | `Equalizer → Bass Enhancer → Stereo Tools → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/cinema-01.md](../../measurements/datasheets/cinema-01.md) |
| Validation dossier | [validation/profiles/cinema-01.md](../../validation/profiles/cinema-01.md) |
| Limitations | No autogain; not night-mode DRC |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Listening campaign complete — seal **Stable**.
