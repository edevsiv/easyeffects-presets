# Profile dossier — `voice-boost-02`

| Field | Value |
|-------|-------|
| Category | voice |
| Seal | **Stable** |
| File | `presets/voice/voice-boost-02.json` |
| Certification eval (Milestone 02) | Beta OK · Validated PASS · Stable PASS |
| Reference hardware | HW-001 |

## Technical sheet

| Item | Link / value |
|------|----------------|
| Datasheet | [../../measurements/datasheets/voice-boost-02.md](../../measurements/datasheets/voice-boost-02.md) |
| Chain | `autogain#0 → multiband_compressor#0 → equalizer#0 → exciter#0 → bass_enhancer#0 → stereo_tools#0 → limiter#0` |
| History | [../../presets/HISTORY.md](../../presets/HISTORY.md) |
| Version history extras | `measurements/version-history/voice-boost-02-*` |

## Benchmark

Category comparison: [../COMPARE.md](../COMPARE.md) · Matrix: [../../research/FEATURE_MATRIX.md](../../research/FEATURE_MATRIX.md)

## Validation

| Campaign | Evidence |
|----------|----------|
| VC-2026-08 | UI screenshots + ui-load log [../logs/voice-boost-02.md](../logs/voice-boost-02.md) |
| VC-2026-08-LISTEN | [VC-2026-08-LISTEN](../campaigns/VC-2026-08-LISTEN/sessions/20260802-L001-voice-boost-02.md) |

## Results

Subjective MOS: see listening session. Seal **Stable**.

## Hardware tested

| ID | Result |
|----|--------|
| HW-001 | UI load + screenshots + listening Validated→Stable |

## Limitations

Hybrid content chain, not broadcast voice processor.

## Promotion checklist (Beta → Validated → Stable)

- [x] Listening form filed
- [x] A/B vs Flat
- [x] Primary metrics gate
- [x] Fatigue gate
- [x] Reproducibility block
