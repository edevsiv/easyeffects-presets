# Audio profile — `gaming-01`

| Field | Value |
|-------|-------|
| ID | `gaming-01` |
| Category | gaming |
| Objective | Footsteps and positional cues with bright clarity |
| Version | aligned with `v1.0.0-rc1` artifact set |
| Seal | **Beta** |
| License | MIT (repository) |
| Preset JSON | [`presets/gaming/gaming-01.json`](../../presets/gaming/gaming-01.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `gaming`, `headphones`, `notebook` |
| Validated (evidence) | `HW-001` (UI/screenshots; listening pending) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `equalizer`, `bass_enhancer`, `stereo_tools`, `limiter` |
| Pipeline | `Equalizer → Bass Enhancer → Stereo Tools → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/gaming-01.md](../../measurements/datasheets/gaming-01.md) |
| Validation dossier | [validation/profiles/gaming-01.md](../../validation/profiles/gaming-01.md) |
| Limitations | Bright EQ may fatigue |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Validated seal requires listening forms.
