# Audio profile — `classic-music-01`

| Field | Value |
|-------|-------|
| ID | `classic-music-01` |
| Category | music |
| Objective | Light, natural classical / acoustic listening |
| Version | aligned with `v1.0.0` artifact set |
| Seal | **Stable** |
| License | MIT (repository) |
| Preset JSON | [`presets/music/classic-music-01.json`](../../presets/music/classic-music-01.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `headphones`, `usb-dac` |
| Validated (evidence) | `HW-001` (UI + VC-2026-08-LISTEN) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `equalizer`, `stereo_tools`, `reverb`, `limiter` |
| Pipeline | `Equalizer → Stereo Tools → Reverb → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/classic-music-01.md](../../measurements/datasheets/classic-music-01.md) |
| Validation dossier | [validation/profiles/classic-music-01.md](../../validation/profiles/classic-music-01.md) |
| Limitations | Light reverb may annoy purists |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Listening campaign complete — seal **Stable**.
