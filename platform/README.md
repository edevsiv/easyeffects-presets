# EasyEffects Audio Platform

This directory is the **product surface** of the project: an open Linux audio
engineering and calibration platform built around EasyEffects + PipeWire.

Presets under `presets/` remain the shipping DSP artifacts. The platform layer
adds **knowledge, databases, calibration, tools, and community process**.

## Mission

| Before (preset pack) | Now (platform) |
|----------------------|----------------|
| Ship JSON files | Ship knowledge + calibration + profiles + tools |
| “Pick a preset” | “Understand your hardware → calibrate → choose profile” |
| Marketing claims | Evidence gates ([validation/CERTIFICATION.md](../validation/CERTIFICATION.md)) |

## Layout

| Path | Role |
|------|------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | System architecture |
| [database/](database/) | Canonical schema + profile index |
| [audio-profiles/](audio-profiles/) | Profile cards (metadata; JSON lives in `presets/`) |
| [calibration/](calibration/) | Hardware calibration DB index + scorecard bridge |
| [hardware/](hardware/) | Hardware taxonomy + scorecards |
| [dsp/](dsp/) | DSP engineering knowledge base |
| [tools/](tools/) | Search / recommendation designs + CLI notes |
| [community/](community/) | Community program |
| [GOVERNANCE.md](GOVERNANCE.md) | Governance & acceptance |
| [RELEASE_STRATEGY.md](RELEASE_STRATEGY.md) | Nightly → Reference channels |

## Related labs (do not duplicate)

| Lab | Path |
|-----|------|
| Validation / certification | [../validation/](../validation/) |
| Calibration playbooks | [../calibration/](../calibration/) |
| Measurements | [../measurements/](../measurements/) |
| Research | [../research/](../research/) |
| AutoEQ | [../autoeq/](../autoeq/) |
| Impulse responses | [../impulse-responses/](../impulse-responses/) |
| Future website IA | [../docs/site/](../docs/site/) |

## Non-goals (this phase)

- No new preset JSON files
- No automatic mutation of existing presets
- No Stable/Validated seal promotions without listening evidence
