# Profile dossier — `cinema-01`

| Field | Value |
|-------|-------|
| Category | movie |
| Seal | **Stable** |
| File | `presets/movie/cinema-01.json` |
| Certification eval (Milestone 02) | Beta OK · Validated PASS · Stable PASS |
| Reference hardware | HW-001 |

## Technical sheet

| Item | Link / value |
|------|----------------|
| Datasheet | [../../measurements/datasheets/cinema-01.md](../../measurements/datasheets/cinema-01.md) |
| Chain | `equalizer#0 → bass_enhancer#0 → compressor#0 → limiter#0` |
| History | [../../presets/HISTORY.md](../../presets/HISTORY.md) |
| Version history extras | `measurements/version-history/cinema-01-*` |

## Benchmark

Category comparison: [../COMPARE.md](../COMPARE.md) · Matrix: [../../research/FEATURE_MATRIX.md](../../research/FEATURE_MATRIX.md)

## Validation

| Campaign | Evidence |
|----------|----------|
| VC-2026-08 | UI screenshots + ui-load log [../logs/cinema-01.md](../logs/cinema-01.md) |
| VC-2026-08-LISTEN | [VC-2026-08-LISTEN](../campaigns/VC-2026-08-LISTEN/sessions/20260802-L001-cinema-01.md) |

## Results

Subjective MOS: see listening session. Seal **Stable**.

## Hardware tested

| ID | Result |
|----|--------|
| HW-001 | UI load + screenshots + listening Validated→Stable |

## Limitations

No autogain; not night-mode DRC.

## Promotion checklist (Beta → Validated → Stable)

- [x] Listening form filed
- [x] A/B vs Flat
- [x] Primary metrics gate
- [x] Fatigue gate
- [x] Reproducibility block
