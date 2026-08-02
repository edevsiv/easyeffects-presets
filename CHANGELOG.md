# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **FASE 06** EasyEffects Audio Platform layer (`platform/`)
  - Architecture, profile schema + `profiles.json`, 11 audio-profile cards
  - Hardware taxonomy (Realtek/ALC*, DAC, HDMI, BT, speakers, headphones, IEM, …) + HW-001 scorecard
  - DSP knowledge base (multiband, limiter, fatigue, dynamics, stereo, AutoEQ, Convolver, IR)
  - Tools: search design + recommend-by-hardware matrix
  - Community program + governance + release channels (Nightly→Reference)
  - `docs/site/` website information architecture
- AutoEQ `INTEGRATION.md` + `WORKFLOW.md`
- Open IR catalog `SCORECARD.md` + research notes
- Roadmap replanned through **v5.0**

### Changed

- README repositioned as **audio engineering platform** (presets are artifacts)
- No new preset JSON in FASE 06; no seal promotions

### Planned

- FASE 07: listening sessions → Validated → v1.0.0 Stable
- Hardware search CLI + static site from `docs/site/`
- License-cleared IR data release / Convolver workflow

## [1.0.0-rc1] notes carried forward

FASE 04 delivered: VC-2026-08 UI campaign, HW-001, real screenshots, EE8 schema fixes, calibration playbooks, APO parser, IR selection checklist.

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
