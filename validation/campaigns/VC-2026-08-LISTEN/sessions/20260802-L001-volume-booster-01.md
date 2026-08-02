# Listening session — `volume-booster-01`

## Session header

| Field | Value |
|-------|-------|
| Form version | 1.0 |
| Campaign ID | VC-2026-08-LISTEN |
| Session ID | 20260802-L001-volume-booster-01 |
| Date (UTC-4 / local) | 2026-08-02 |
| Listener ID | L-001 (siviero) |
| Hardware ID | HW-001 |
| Distro | Linux Mint 22.3 |
| Kernel | 7.0.0-28-generic |
| PipeWire version | 1.0.5 · float32le 2ch 48000Hz |
| EasyEffects version / install | Flatpak 8.2.8 |
| Quantum / rate | ~1024 / 48000 Hz |
| Content class | Streaming |
| Content title / URL (no redistribution) | Quiet stream / system media (experimental loudness) |
| Preset under test | `volume-booster-01` |
| Comparison anchors | Flat (EE bypass) / sibling when noted |
| System volume | Comfortable desktop level; level-matched vs Flat |
| EE bypass used for level match? | Yes |
| Listening duration (minutes) | 12 |
| Environment | Typical room |

## Scores (1.0–5.0, half-steps allowed)

| Metric | Score | Comment |
|--------|------:|---------|
| Voice Clarity | 3.0 | Louder not clearer |
| Bass | 3.0 | Boosted |
| Treble | 3.0 | OK |
| Stereo | 2.5 | Narrow |
| Dynamic Range | 3.0 | Squashed |
| Fatigue | 2.5 | Fatiguing when loud |
| Immersion | 2.5 | Not goal |
| Naturalness | 2.5 | Obvious boost |
| Overall | 2.8 | Below Validated bar |

## Gate evaluation (CERTIFICATION V1–V6)

| Gate | Result | Notes |
|------|--------|-------|
| V1 Form filed | PASS | This file |
| V2 Content class | PASS | Streaming |
| V3 A/B vs Flat | PASS | Documented below |
| V4 Primary metrics | FAIL | primaries ['Bass', 'Overall']: mean=2.90, min=2.8 |
| V5 Fatigue | WAIVER/FAIL | Short-session waiver — fatigue gate not claimed for promotion. |
| V6 Reproducibility | PASS | See validation/reproducibility/HW-001.md · ENVIRONMENT.md |

## Free-form comments

A/B vs Flat: useful loudness tool but fails V4/V5. Keep Beta. Short-session waiver (fatigue claim not asserted).

Load verified on HW-001 with EasyEffects 8.2.8 (`flatpak run … -l volume-booster-01`). Evidence type: `subjective-log` + prior `design-audit` / ui-load.

Target seal after evaluation: **Beta**.

## Verdict

- [ ] Promote candidate (meets gates in CERTIFICATION.md)
- [x] Keep current seal
- [ ] Regress / demote
- [ ] Iterate parameters (open engineering issue)

## Signature

Listener: L-001 / siviero  Date: 2026-08-02
