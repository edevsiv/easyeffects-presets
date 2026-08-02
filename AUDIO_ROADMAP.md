# Audio technical roadmap

Engineering roadmap for the **EasyEffects Audio Platform** (knowledge, calibration, research, profiles, and tools for Linux audio) through **v5.0**.

Related: [CHANGELOG.md](CHANGELOG.md) · [platform/](platform/) · [platform/RELEASE_STRATEGY.md](platform/RELEASE_STRATEGY.md)

## Vision

Become the primary **open-source Linux audio engineering platform** around EasyEffects + PipeWire by combining:

1. Auditable DSP profiles
2. Hardware calibration & scorecards
3. DSP knowledge base (why / when / how)
4. Research mappings from commercial suites
5. Strict listening / certification protocol
6. Tools that recommend — without silently rewriting user chains

## Version plan

### v1.x — Laboratory foundation (done → in progress)

| Track | Status |
|-------|--------|
| Repo scaffold, CI, install scripts | Done (FASE 01) |
| Research lab + feature matrix | Done (FASE 02) |
| Metrics, datasheets, design-audit | Done (FASE 03) |
| UI validation campaign + RC1 | Done (FASE 04) |
| Certification / listening program | Done scaffolding (FASE 05) |
| **Audio Platform layer** | **Done scaffolding (FASE 06)** |
| Human listening sessions on P0 hardware | **Done** (VC-2026-08-LISTEN → v1.0.0) |

**Exit criteria for listening-validated v1.0.0 Stable:** [release/CHECKLIST_v1.0.0.md](release/CHECKLIST_v1.0.0.md) — **met**.

### v1.1 — Evidence & hardware expansion

- Multi-listener sessions toward Reference seals
- First community hardware scorecards beyond HW-001
- See [release/POST_RELEASE.md](release/POST_RELEASE.md)

### v1.2 — FxSound / Dolby-inspired refinement

- Parameter translation tables kept current
- Optional enhancer splits (clarity / bass) — only with datasheets
- Cinema night-mode profile (stronger DRC) when methodology OK

### v2.0 — Correction & convolution platform

- AutoEQ CLI recommend path mature ([autoeq/INTEGRATION.md](autoeq/INTEGRATION.md))
- First Convolver workflows with scored open IRs
- Optional `no-eq` content profile variants (manual apply)

### v2.1 — Gaming & routing

- PipeWire ChatMix-like documentation
- Competitive vs immersive pairs validated on multiple titles
- Input (mic) profile pack draft

### v3.0 — Laboratory maturity

- Aggregated blind A/B notes
- Methodology paper-style doc
- Stable profile metadata conventions
- Packaging helpers (AUR/Nix optional)

### v4.0 — Website & search

- Static site from [docs/site/](docs/site/)
- Hardware → profile search UI
- Published dashboards from validation statistics

### v5.0 — Platform completeness

- Multi-HW Reference seals for core categories
- Community calibration corpus (≥20 listening logs)
- Optional offline recommender reading `platform/database/profiles.json`
- IR data releases (license-cleared) separate from code tags

## Architecture (target)

```text
Hardware identity → Calibration → Search/recommend → Profile card → JSON artifact
                           ↘ AutoEQ / Convolver layers
                                    ↓
                           Listening → Certification seals → Release channel
```

## Non-goals

- Bit-identical clones of Dolby/DTS/Nahimic
- Shipping copyrighted media or proprietary IR databases
- Silent auto-edit of user presets
- Replacing EasyEffects upstream development

## Success metrics

| Metric | Target by v5.0 |
|--------|----------------|
| Profiles with complete cards + HISTORY | 100% |
| Hardware classes with ≥1 scorecard | ≥ 10 |
| Open IR workflows documented | ≥ 5 |
| Contributor listening sessions merged | ≥ 20 |
| Site routes implemented | docs/site IA live |
| CI + governance on DSP/seal PRs | Required |
