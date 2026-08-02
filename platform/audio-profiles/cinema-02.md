# Audio profile — `cinema-02`

| Field | Value |
|-------|-------|
| ID | `cinema-02` |
| Category | movie |
| Objective | Premium cinematic stack with autogain and multiband dynamics |
| Version | aligned with `v1.0.0-rc1` artifact set |
| Seal | **Beta** |
| License | MIT (repository) |
| Preset JSON | [`presets/movie/cinema-02.json`](../../presets/movie/cinema-02.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `notebook`, `speakers-2.0` |
| Validated (evidence) | `HW-001` (UI/screenshots; listening pending) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `autogain`, `multiband_compressor`, `equalizer`, `exciter`, `bass_enhancer`, `stereo_tools`, `limiter` |
| Pipeline | `Autogain → Multiband Compressor → Equalizer → Exciter → Bass Enhancer → Stereo Tools → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/cinema-02.md](../../measurements/datasheets/cinema-02.md) |
| Validation dossier | [validation/profiles/cinema-02.md](../../validation/profiles/cinema-02.md) |
| Limitations | Heavy chain; fatigue risk |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Validated seal requires listening forms.
