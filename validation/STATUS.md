# Validation status seals

| Seal | Meaning |
|------|---------|
| Experimental | Ships for testing; known risks / incomplete evidence |
| Beta | Loads on reference HW with screenshots; listening incomplete or gates unmet |
| Validated | Passed certification listening gates on ≥1 P0 device |
| Stable | Validated + release regression gates |
| Reference | Multi-listener / multi-HW gold standard |

Criteria: [CERTIFICATION.md](CERTIFICATION.md)

## Current seals (Milestone 02 / 2026-08-02)

| Preset | Seal | Notes |
|--------|------|-------|
| `cinema-01` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `cinema-02` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `music-hd-01` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `music-hd-02` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `classic-music-01` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `gaming-01` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `gaming-02` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `voice-boost-01` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `voice-boost-02` | **Stable** | VC-2026-08-LISTEN V1–V6 + S1–S4 |
| `volume-booster-01` | **Beta** | Listening filed; V4/V5 not met |
| `fxsound-ultimate-02` | **Experimental** | Enhancer showcase; fatigue gate fail |

## Promotion log (VC-2026-08-LISTEN)

| Preset | From | To | Reason |
|--------|------|----|--------|
| `cinema-01` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `cinema-02` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `music-hd-01` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `music-hd-02` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `classic-music-01` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `gaming-01` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `gaming-02` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `voice-boost-01` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `voice-boost-02` | Beta | Stable | V1–V6 + Stable S1–S4 on HW-001 |
| `volume-booster-01` | Beta | Beta | V4/V5 fail — keep |
| `fxsound-ultimate-02` | Experimental | Experimental | Fatigue gate fail — keep |

**v1.0.0 Stable:** **GO** for promoted profiles (9 Stable · 1 Beta · 1 Experimental).
