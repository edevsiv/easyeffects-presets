# Profile dossier — `music-hd-02`

| Field | Value |
|-------|-------|
| Category | music |
| Seal | **Beta** |
| File | `presets/music/music-hd-02.json` |
| Certification eval (FASE 05) | Beta OK · Validated FAIL (no listening form) |
| Reference hardware | HW-001 |

## Technical sheet

| Item | Link / value |
|------|----------------|
| Datasheet | [../../measurements/datasheets/music-hd-02.md](../../measurements/datasheets/music-hd-02.md) |
| Chain | `autogain#0 → multiband_compressor#0 → equalizer#0 → exciter#0 → bass_enhancer#0 → stereo_tools#0 → limiter#0` |
| History | [../../presets/HISTORY.md](../../presets/HISTORY.md) |
| Version history extras | `measurements/version-history/music-hd-02-*` |

## Benchmark

Category comparison: [../COMPARE.md](../COMPARE.md) · Matrix: [../../research/FEATURE_MATRIX.md](../../research/FEATURE_MATRIX.md)

## Validation

| Campaign | Evidence |
|----------|----------|
| VC-2026-08 | UI screenshots + ui-load log [../logs/music-hd-02.md](../logs/music-hd-02.md) |
| VC-2026-08-LISTEN | _pending_ |

## Results

See [../logs/music-hd-02.md](../logs/music-hd-02.md) (design-audit + ui-load scores). Subjective MOS: none yet.

## Hardware tested

| ID | Result |
|----|--------|
| HW-001 | UI load + screenshots |

## Limitations

Not fidelity-first; enhancer density.

## Promotion checklist (Beta → Validated)

- [ ] Listening form filed
- [ ] A/B vs Flat
- [ ] Primary metrics gate
- [ ] Fatigue gate
- [ ] Reproducibility block
