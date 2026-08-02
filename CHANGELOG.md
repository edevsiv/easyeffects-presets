# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Official validation campaign **VC-2026-08** (`validation/`)
- Hardware database entry HW-001 (Acer Nitro AN515-51, Realtek ALC255)
- Real EasyEffects 8.2.8 PNG screenshots for all presets
- Validation seals (Experimental / Beta / …)
- Calibration playbooks (`calibration/`)
- AutoEQ experimental APO parser script
- Open IR selection checklist
- Release candidate notes + preset ZIP (`release/`)
- Screenshot capture scripts

### Changed

- EasyEffects 8 compatibility: migrate legacy `bass_enhancer` scope/blend and `limiter` schema on `*-01` presets
- `scripts/install.sh` prefers Flatpak XDG **data** output path (EE8)
- README gallery uses PNG captures instead of SVG placeholders

### Planned

- Subjective A/B logs per category → Validated seals → v1.0.0 Stable
- Filled measurement logs for all presets on more devices
- Additional headphone-oriented EQ profiles (AutoEQ overlays)
- Autoload examples for application-specific routing

## [1.0.0-rc1] - 2026-08-02

Release candidate bundling FASE 01–04: repository scaffold, research lab, DSP engineering, and first UI validation campaign.

See [release/NOTES_v1.0.0-rc1.md](release/NOTES_v1.0.0-rc1.md).


## [1.0.0] - 2026-08-02

### Added

- Initial public repository structure for EasyEffects Presets Premium
- Categorized output presets: movie, music, gaming, voice, experimental
- Full open-source documentation set (README, INSTALL, PIPEWIRE, MPV, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT)
- Install and validation scripts under `scripts/`
- Example `mpv.conf` and PipeWire notes
- GitHub Actions workflow to validate JSON presets and repository structure
- SVG screenshot placeholders

### Presets

| Preset | Category |
|--------|----------|
| cinema-01 / cinema-02 | movie |
| music-hd-01 / music-hd-02 / classic-music-01 | music |
| gaming-01 / gaming-02 | gaming |
| voice-boost-01 / voice-boost-02 | voice |
| volume-booster-01 / fxsound-ultimate-02 | experimental |

[Unreleased]: https://github.com/edevsiv/easyeffects-presets/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/edevsiv/easyeffects-presets/releases/tag/v1.0.0
