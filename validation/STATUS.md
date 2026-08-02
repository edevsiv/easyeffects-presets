# Validation status seals

| Seal | Meaning |
|------|---------|
| Experimental | Ships for testing; known risks / incomplete evidence |
| Beta | Loads on reference HW with screenshots; listening incomplete |
| Validated | Passed campaign metrics on ≥1 P0 device with A/B log |
| Stable | Validated + no critical regressions across releases |
| Reference | Community gold standard for a category |

## Current seals (VC-2026-08)

| Preset | Seal | Notes |
|--------|------|-------|
| `cinema-01` | **Beta** | EE8 compat fixes + UI screenshots on HW-001 |
| `cinema-02` | **Beta** | UI screenshots on HW-001; heavy chain |
| `music-hd-01` | **Beta** | EE8 limiter migration + UI screenshots |
| `music-hd-02` | **Beta** | UI screenshots; enhancer chain |
| `classic-music-01` | **Beta** | EE8 limiter migration + UI screenshots |
| `gaming-01` | **Beta** | EE8 bass/limiter fixes + UI screenshots |
| `gaming-02` | **Beta** | UI screenshots; immersion chain |
| `voice-boost-01` | **Beta** | EE8 limiter migration + UI screenshots |
| `voice-boost-02` | **Beta** | UI screenshots after FASE03 trim |
| `volume-booster-01` | **Beta** | EE8 limiter migration + UI screenshots |
| `fxsound-ultimate-02` | **Experimental** | Enhancer showcase; UI screenshots; listening pending |

No preset is **Validated** / **Stable** / **Reference** until subjective A/B logs are filed under `validation/logs/`.
