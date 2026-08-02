# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Research laboratory (`research/`) covering FxSound, Dolby, DTS:X, SteelSeries Sonar, Peace/APO, Realtek, Waves MaxxAudio, Nahimic, EasyEffects, PipeWire, Linux audio
- Feature matrix mapping commercial capabilities to EasyEffects plugins
- Audio engine handbook under `docs/audio-engine/`
- Official listening test protocol and measurement log template
- Reference content library (`references/`)
- Documentary benchmark (`benchmark/`)
- `AUDIO_ROADMAP.md` through v3.0
- Preset history ledger (`presets/HISTORY.md`)
- Placeholders for `autoeq/` and `impulse-responses/`
- Architecture and benchmark SVG diagrams

### Planned

- Real screenshots of EasyEffects graphs per preset
- Filled measurement logs for all presets
- Additional headphone-oriented EQ profiles
- Autoload examples for application-specific routing
- Flatpak one-liner installer improvements

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
