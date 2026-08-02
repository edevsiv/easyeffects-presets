# Audio profile — `music-hd-01`

| Field | Value |
|-------|-------|
| ID | `music-hd-01` |
| Category | music |
| Objective | Musical clarity with controlled enhancement |
| Version | aligned with `v1.0.0-rc1` artifact set |
| Seal | **Beta** |
| License | MIT (repository) |
| Preset JSON | [`presets/music/music-hd-01.json`](../../presets/music/music-hd-01.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `headphones`, `usb-dac`, `notebook` |
| Validated (evidence) | `HW-001` (UI/screenshots; listening pending) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `equalizer`, `bass_enhancer`, `stereo_tools`, `limiter` |
| Pipeline | `Equalizer → Bass Enhancer → Stereo Tools → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/music-hd-01.md](../../measurements/datasheets/music-hd-01.md) |
| Validation dossier | [validation/profiles/music-hd-01.md](../../validation/profiles/music-hd-01.md) |
| Limitations | No AutoEQ correction yet |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Validated seal requires listening forms.
