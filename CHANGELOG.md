# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Community multi-listener sessions toward Reference seals
- Hardware scorecards beyond HW-001
- AutoEQ / Convolver user workflows; static site from `docs/site/`

## [1.0.0] - 2026-08-02

### Added

- Official listening campaign **VC-2026-08-LISTEN** (11 sessions on HW-001 / L-001)
- Release notes, presets ZIP, distro install notes, post-release checklist, final audit
- EasyEffects Audio Platform layer (`platform/`) from FASE 06
- Certification program, UI campaign evidence, datasheets, research lab (FASE 01–05)

### Changed

- **9** profiles promoted Beta → Validated → **Stable**
- README focused on Quick Start, Downloads, Profiles, Hardware, FAQ
- Flatpak installer targets EE8 `data/easyeffects/output` (avoids config migrate/trash)

### Seals

| Seal | Presets |
|------|---------|
| Stable | cinema-01/02, music-hd-01/02, classic-music-01, gaming-01/02, voice-boost-01/02 |
| Beta | volume-booster-01 |
| Experimental | fxsound-ultimate-02 |

See [release/NOTES_v1.0.0.md](release/NOTES_v1.0.0.md).

## [1.0.0-rc1] - 2026-08-02

Release candidate bundling FASE 01–04: repository scaffold, research lab, DSP engineering, and first UI validation campaign.

See [release/NOTES_v1.0.0-rc1.md](release/NOTES_v1.0.0-rc1.md).

[Unreleased]: https://github.com/edevsiv/easyeffects-presets/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/edevsiv/easyeffects-presets/releases/tag/v1.0.0
[1.0.0-rc1]: https://github.com/edevsiv/easyeffects-presets/releases/tag/v1.0.0-rc1
