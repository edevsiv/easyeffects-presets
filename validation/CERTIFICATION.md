# Certification program — promotion criteria

Seals advance only when **objective gates** pass. No opinion-only promotions.

## Seal ladder

```text
Experimental → Beta → Validated → Stable → Reference
```

## Gates

### Experimental → Beta

| # | Gate | Evidence |
|---|------|----------|
| B1 | Valid EasyEffects JSON + CI | `scripts/validate.sh` |
| B2 | Datasheet + HISTORY entry | `measurements/datasheets/`, `presets/HISTORY.md` |
| B3 | UI load on ≥1 registered HW | screenshot or ui-load log |
| B4 | No blocking schema errors on reference EE | campaign note |

### Beta → Validated

| # | Gate | Evidence |
|---|------|----------|
| V1 | ≥1 filled listening form ([forms/LISTENING_FORM.md](forms/LISTENING_FORM.md)) | `campaigns/*/sessions/` |
| V2 | Content class matches category (≥1 of film/music/game/speech/…) | form field |
| V3 | A/B vs Flat documented | [AB_TESTING](../docs/methodology/AB_TESTING.md) |
| V4 | Primary metrics ≥ **3.5** mean; no primary metric < **3.0** | form scores |
| V5 | Fatigue ≥ **3.0** after ≥15 min **or** explicit short-session waiver | form |
| V6 | Reproducibility block completed | [reproducibility/](reproducibility/) |

### Validated → Stable

| # | Gate | Evidence |
|---|------|----------|
| S1 | Validated on reference HW | HW-001 or successor |
| S2 | No critical EE-load regression on current major EE | retest note |
| S3 | Changelog entry for certified revision | CHANGELOG |
| S4 | Release checklist subjective items checked | `release/CHECKLIST_v1.0.0.md` |

### Stable → Reference

| # | Gate | Evidence |
|---|------|----------|
| R1 | ≥3 independent listener sessions **or** 2 HW classes | listeners DB |
| R2 | Category community consensus note | report |
| R3 | Maintainer designation | STATUS.md |

## FASE 05 evaluation (2026-08-02)

| Gate set | Result |
|----------|--------|
| Beta gates (shipping presets with UI evidence) | **PASS** (from VC-2026-08) |
| Validated gates | **PASS** (VC-2026-08-LISTEN — 9 presets) |
| Stable | **PASS** (S1–S4 on HW-001 for those 9) |
| Reference | **FAIL** — needs multi-listener / multi-HW |

**Promotion actions (Milestone 02):** 9 presets Beta → Validated → **Stable**.  
`volume-booster-01` remains **Beta** (V4/V5 unmet).  
`fxsound-ultimate-02` remains **Experimental** (fatigue gate).
