# Profile dossier — `music-hd-02`

| Field | Value |
|-------|-------|
| Category | music |
| Seal | **Stable** |
| File | `presets/music/music-hd-02.json` |
| Certification eval (Milestone 02) | Beta OK · Validated PASS · Stable PASS |
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
| VC-2026-08-LISTEN | [VC-2026-08-LISTEN](../campaigns/VC-2026-08-LISTEN/sessions/20260802-L001-music-hd-02.md) |

## Results

Subjective MOS: see listening session. Seal **Stable**.

## Hardware tested

| ID | Result |
|----|--------|
| HW-001 | UI load + screenshots + listening Validated→Stable |

## Limitations

Not fidelity-first; enhancer density.

## Promotion checklist (Beta → Validated → Stable)

- [x] Listening form filed
- [x] A/B vs Flat
- [x] Primary metrics gate
- [x] Fatigue gate
- [x] Reproducibility block
