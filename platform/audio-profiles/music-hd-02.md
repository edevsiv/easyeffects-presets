# Audio profile — `music-hd-02`

| Field | Value |
|-------|-------|
| ID | `music-hd-02` |
| Category | music |
| Objective | Fuller music enhancer stack |
| Version | aligned with `v1.0.0-rc1` artifact set |
| Seal | **Beta** |
| License | MIT (repository) |
| Preset JSON | [`presets/music/music-hd-02.json`](../../presets/music/music-hd-02.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `headphones`, `speakers-2.0` |
| Validated (evidence) | `HW-001` (UI/screenshots; listening pending) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `autogain`, `multiband_compressor`, `equalizer`, `exciter`, `bass_enhancer`, `stereo_tools`, `limiter` |
| Pipeline | `Autogain → Multiband → EQ → Exciter → Bass → Stereo → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/music-hd-02.md](../../measurements/datasheets/music-hd-02.md) |
| Validation dossier | [validation/profiles/music-hd-02.md](../../validation/profiles/music-hd-02.md) |
| Limitations | Not fidelity-first |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Validated seal requires listening forms.
