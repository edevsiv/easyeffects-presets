# Profile dossier — `volume-booster-01`

| Field | Value |
|-------|-------|
| Category | experimental |
| Seal | **Beta** |
| File | `presets/experimental/volume-booster-01.json` |
| Certification eval (FASE 05) | Beta OK · Validated FAIL (no listening form) |
| Reference hardware | HW-001 |

## Technical sheet

| Item | Link / value |
|------|----------------|
| Datasheet | [../../measurements/datasheets/volume-booster-01.md](../../measurements/datasheets/volume-booster-01.md) |
| Chain | `equalizer#0 → compressor#0 → limiter#0` |
| History | [../../presets/HISTORY.md](../../presets/HISTORY.md) |
| Version history extras | `measurements/version-history/volume-booster-01-*` |

## Benchmark

Category comparison: [../COMPARE.md](../COMPARE.md) · Matrix: [../../research/FEATURE_MATRIX.md](../../research/FEATURE_MATRIX.md)

## Validation

| Campaign | Evidence |
|----------|----------|
| VC-2026-08 | UI screenshots + ui-load log [../logs/volume-booster-01.md](../logs/volume-booster-01.md) |
| VC-2026-08-LISTEN | _pending_ |

## Results

See [../logs/volume-booster-01.md](../logs/volume-booster-01.md) (design-audit + ui-load scores). Subjective MOS: none yet.

## Hardware tested

| ID | Result |
|----|--------|
| HW-001 | UI load + screenshots |

## Limitations

Crude flat +2 dB shelf.

## Promotion checklist (Beta → Validated)

- [ ] Listening form filed
- [ ] A/B vs Flat
- [ ] Primary metrics gate
- [ ] Fatigue gate
- [ ] Reproducibility block
