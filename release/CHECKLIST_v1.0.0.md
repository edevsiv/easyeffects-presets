# Release checklist — v1.0.0

## Product

- [x] Presets categorized and named kebab-case
- [x] Install + validate scripts
- [x] Research lab + feature matrix
- [x] Metrics + datasheets + test matrix
- [x] A/B + listening protocols
- [ ] At least one filled subjective A/B log per category (P0)
- [ ] Real EasyEffects screenshots (replace SVG placeholders)
- [x] LICENSE MIT, SECURITY, CoC, CONTRIBUTING

## Engineering

- [x] FASE 03 design-audit of all presets
- [x] Version history for JSON changes
- [ ] Human confirmation of FASE 03 optimizations
- [x] CI workflow present
- [x] `./scripts/validate.sh` passes
- [x] Markdown links pass

## GitHub release steps

1. Ensure `main` green CI
2. Update CHANGELOG `[1.0.0]` section with FASE 02–03 notes if tagging now
3. `git tag -a v1.0.0 -m "v1.0.0"`
4. `git push origin v1.0.0`
5. GitHub Release notes from CHANGELOG
6. Set repository topics (easyeffects, pipewire, …)
7. Copy datasheet summary into `measurements/reference-results/`

## Go / no-go

**Conditional go:** documentation and engineering baseline are release-candidate quality.  
**Blockers for “scientifically listening-validated” claim:** missing filled A/B logs on real hardware.
