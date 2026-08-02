# Audio technical roadmap

Engineering roadmap for EasyEffects Presets Premium from the current laboratory baseline toward **v3.0**.

Related: [CHANGELOG.md](CHANGELOG.md) · [research/](research/) · [docs/methodology/TEST_PROTOCOL.md](docs/methodology/TEST_PROTOCOL.md)

## Vision

Become the primary **open-source reference** for EasyEffects presets by combining:

1. Auditable DSP chains
2. Documented mappings from commercial suites
3. Strict listening protocol
4. Measurement-friendly workflow

## Version plan

### v1.x — Foundation (current)

| Track | Status |
|-------|--------|
| Repo scaffold, CI, install scripts | Done (FASE 01) |
| Research lab + feature matrix | Done (FASE 02) |
| Audio engine handbook | Done (FASE 02) |
| Official test protocol | Done (FASE 02) |
| Documentary benchmark | Done (FASE 02) |
| Preset history ledger | Done (FASE 02) |
| Metrics + datasheets + hardware bank | Done (FASE 03) |
| A/B protocol + FxSound mapping | Done (FASE 03) |
| Design-audit optimization of `*-02` | Done (FASE 03) |
| AutoEQ architecture + IR catalog | Done (FASE 03, design only) |
| Human A/B logs on P0 hardware | Pending |

**Exit criteria for listening-validated v1.0.0:** checklist in [release/CHECKLIST_v1.0.0.md](release/CHECKLIST_v1.0.0.md).

### v1.1 — Listening iteration

- Fill `measurements/` with real logs for all 11 presets
- Replace SVG screenshot placeholders with UI captures
- Tune `*-01` presets for fatigue reduction
- Publish first “known good devices” notes (2–3 headphones)

### v1.2 — FxSound / Dolby inspired refinement

- Parameter translation tables (FxSound knobs → EE plugins)
- Split experimental enhancer into `fxsound-clarity` / `fxsound-bass` variants
- Cinema night mode (stronger DRC, quieter peaks)

### v2.0 — Correction & convolution

- Populate `autoeq/` conversion tooling
- First Convolver-based headphone correction presets
- Curated open IRs under `impulse-responses/`
- Optional per-device preset naming scheme

### v2.1 — Gaming routing

- Document PipeWire ChatMix-like setups
- Competitive vs immersive gaming pairs validated on 3 titles each
- Input preset pack draft (mic)

### v3.0 — Laboratory maturity

- Blind A/B harness notes + aggregated scores
- Public “methodology paper” style doc in `docs/`
- Stable preset API/versioning (`preset_version` metadata where feasible)
- Packaging (AUR/Nix/optional) and tagged data releases for IRs

## Architecture of presets (target)

```text
Content category → Chain archetype → Plugin parameters → Protocol → Measurement log → Release
                       ↑
              research/FEATURE_MATRIX.md
```

## Non-goals

- Bit-identical clones of Dolby/DTS/Nahimic
- Shipping copyrighted media or proprietary IR databases
- Replacing EasyEffects upstream development

## Success metrics

| Metric | Target by v3.0 |
|--------|----------------|
| Presets with complete history + logs | 100% |
| Commercial features mapped | Matrix kept current |
| Open HRTF/correction presets | ≥ 5 documented |
| Contributor test logs merged | ≥ 20 |
| CI + protocol compliance | Required on DSP PRs |
