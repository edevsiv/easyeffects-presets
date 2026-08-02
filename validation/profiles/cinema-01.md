# Profile dossier — `cinema-01`

| Field | Value |
|-------|-------|
| Category | movie |
| Seal | **Beta** |
| File | `presets/movie/cinema-01.json` |
| Certification eval (FASE 05) | Beta OK · Validated FAIL (no listening form) |
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
| VC-2026-08-LISTEN | _pending_ |

## Results

See [../logs/cinema-01.md](../logs/cinema-01.md) (design-audit + ui-load scores). Subjective MOS: none yet.

## Hardware tested

| ID | Result |
|----|--------|
| HW-001 | UI load + screenshots |

## Limitations

No autogain; not night-mode DRC.

## Promotion checklist (Beta → Validated)

- [ ] Listening form filed
- [ ] A/B vs Flat
- [ ] Primary metrics gate
- [ ] Fatigue gate
- [ ] Reproducibility block
