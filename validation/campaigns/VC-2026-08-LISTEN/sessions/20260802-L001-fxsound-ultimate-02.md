# Listening session — `fxsound-ultimate-02`

## Session header

| Field | Value |
|-------|-------|
| Form version | 1.0 |
| Campaign ID | VC-2026-08-LISTEN |
| Session ID | 20260802-L001-fxsound-ultimate-02 |
| Date (UTC-4 / local) | 2026-08-02 |
| Listener ID | L-001 (siviero) |
| Hardware ID | HW-001 |
| Distro | Linux Mint 22.3 |
| Kernel | 7.0.0-28-generic |
| PipeWire version | 1.0.5 · float32le 2ch 48000Hz |
| EasyEffects version / install | Flatpak 8.2.8 |
| Quantum / rate | ~1024 / 48000 Hz |
| Content class | Music |
| Content title / URL (no redistribution) | Enhancer showcase mix (experimental) |
| Preset under test | `fxsound-ultimate-02` |
| Comparison anchors | Flat (EE bypass) / sibling when noted |
| System volume | Comfortable desktop level; level-matched vs Flat |
| EE bypass used for level match? | Yes |
| Listening duration (minutes) | 12 |
| Environment | Typical room |

## Scores (1.0–5.0, half-steps allowed)

| Metric | Score | Comment |
|--------|------:|---------|
| Voice Clarity | 3.0 | OK |
| Bass | 4.0 | Heavy |
| Treble | 3.5 | Excited |
| Stereo | 4.0 | Wide |
| Dynamic Range | 3.5 | Dense |
| Fatigue | 2.5 | Fatiguing |
| Immersion | 3.5 | Fun |
| Naturalness | 2.5 | Highly processed |
| Overall | 3.2 | Showcase only |

## Gate evaluation (CERTIFICATION V1–V6)

| Gate | Result | Notes |
|------|--------|-------|
| V1 Form filed | PASS | This file |
| V2 Content class | PASS | Music |
| V3 A/B vs Flat | PASS | Documented below |
| V4 Primary metrics | PASS | primaries ['Bass', 'Overall']: mean=3.60, min=3.2 |
| V5 Fatigue | WAIVER/FAIL | Short-session waiver — fatigue gate not claimed for promotion. |
| V6 Reproducibility | PASS | See validation/reproducibility/HW-001.md · ENVIRONMENT.md |

## Free-form comments

A/B vs Flat: impressive demo; fails fatigue gate. Remains Experimental. Short-session waiver.

Load verified on HW-001 with EasyEffects 8.2.8 (`flatpak run … -l fxsound-ultimate-02`). Evidence type: `subjective-log` + prior `design-audit` / ui-load.

Target seal after evaluation: **Experimental**.

## Verdict

- [ ] Promote candidate (meets gates in CERTIFICATION.md)
- [x] Keep current seal
- [ ] Regress / demote
- [ ] Iterate parameters (open engineering issue)

## Signature

Listener: L-001 / siviero  Date: 2026-08-02
