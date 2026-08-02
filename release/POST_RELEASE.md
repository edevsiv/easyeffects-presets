# Post-release checklist

After **v1.0.0** ships. Track follow-ups without blocking the Stable cut.

## v1.0.1 — Patch

- [ ] Community bug reports from first week of Stable use
- [ ] Fix any EE 8.x load regressions on non-HW-001 machines
- [ ] README / INSTALL clarifications from user feedback
- [ ] Re-run `validate.sh` + link check on hotfixes
- [ ] Tag `v1.0.1` only for fixes (no new profile seals required)

## v1.1 — Evidence & hardware

- [ ] Second listener (L-002+) on ≥1 Stable profile toward Reference
- [ ] Hardware scorecard beyond HW-001 (USB DAC or headphones class)
- [ ] Promote `volume-booster-01` only if V4/V5 pass on a dedicated session
- [ ] Night-mode / DRC cinema variant (datasheet-first)
- [ ] Hardware search CLI sketch from `platform/tools/`

## v2.0 — Correction platform

- [ ] AutoEQ recommend path documented end-to-end for users
- [ ] First Convolver workflow with license-cleared open IR
- [ ] Optional `no-eq` content variants
- [ ] Input (mic) profile pack draft
- [ ] Static site from `docs/site/` (MVP)

## Always-on hygiene

- [ ] Watch EasyEffects upstream for schema breaks
- [ ] Keep `profiles.json` seals in sync with `validation/STATUS.md`
- [ ] Prefer evidence PRs (`listening: <preset> on <HW-ID>`) over taste-only
