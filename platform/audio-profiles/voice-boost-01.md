# Audio profile — `voice-boost-01`

| Field | Value |
|-------|-------|
| ID | `voice-boost-01` |
| Category | voice |
| Objective | Speech intelligibility boost (output) |
| Version | aligned with `v1.0.0-rc1` artifact set |
| Seal | **Beta** |
| License | MIT (repository) |
| Preset JSON | [`presets/voice/voice-boost-01.json`](../../presets/voice/voice-boost-01.json) |

## Hardware

| Kind | IDs / classes |
|------|----------------|
| Recommended | `notebook`, `headphones` |
| Validated (evidence) | `HW-001` (UI/screenshots; listening pending) |

## DSP

| Item | Value |
|------|-------|
| Plugins | `equalizer`, `compressor`, `deesser`, `limiter` |
| Pipeline | `Equalizer → Compressor → De-esser → Limiter` |

## History · Limitations · Compatibility

| Item | Link / note |
|------|-------------|
| History | [presets/HISTORY.md](../../presets/HISTORY.md) · datasheet [measurements/datasheets/voice-boost-01.md](../../measurements/datasheets/voice-boost-01.md) |
| Validation dossier | [validation/profiles/voice-boost-01.md](../../validation/profiles/voice-boost-01.md) |
| Limitations | Output-only; not mic chain |
| Compatibility | EasyEffects 8.x Flatpak verified on HW-001; PipeWire 48 kHz typical |

## Certification

See [validation/CERTIFICATION.md](../../validation/CERTIFICATION.md). Validated seal requires listening forms.
