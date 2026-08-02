# Audio profile — `voice-boost-02`

| Field | Value |
|-------|-------|
| ID | `voice-boost-02` |
| Category | voice |
| Objective | Richer hybrid speech / content chain |
| Version | aligned with `v1.0.0` artifact set |
| Seal | **Stable** |
| License | MIT (repository) |
| Preset JSON | [`presets/voice/voice-boost-02.json`](../../presets/voice/voice-boost-02.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `notebook`, `speakers-2.0` |
| Validated (evidence) | `HW-001` (UI + VC-2026-08-LISTEN) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `autogain`, `equalizer`, `compressor`, `exciter`, `stereo_tools`, `limiter` |
| Pipeline | `Autogain → EQ → Compressor → Exciter → Stereo → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/voice-boost-02.md](../../measurements/datasheets/voice-boost-02.md) |
| Validation dossier | [validation/profiles/voice-boost-02.md](../../validation/profiles/voice-boost-02.md) |
| Limitations | Not a broadcast voice processor |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Listening campaign complete — seal **Stable**.
