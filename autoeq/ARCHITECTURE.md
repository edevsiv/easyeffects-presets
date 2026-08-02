# AutoEQ integration architecture (design only)

**Status:** designed in FASE 03 — **not implemented** as automation yet.

## Goals

1. Allow headphone-specific correction without forking every content preset.
2. Prefer **Harman** targets (OE 2018 / IE 2019v2) as default research baseline.
3. Keep correction separable from “fun” enhancers (bass/exciter/width).

## Recommended topology

```text
[AutoEQ Equalizer bands] → [Category preset chain without conflicting EQ]
   or
[Category chain using EQ for taste only] + documented “set AutoEQ first” workflow
```

**Preferred v2 approach:** two-layer user workflow

1. Import AutoEQ `ParametricEQ.txt` into EasyEffects Equalizer via **APO** button.
2. Apply a **content** preset that either (a) bypasses its own EQ or (b) is published as `no-eq` variant later.

Until variants exist: document that stacking AutoEQ + smile-curve music EQ is a known interaction risk.

## How to integrate (manual today)

1. Measure or pick headphones on [AutoEQ](https://github.com/jaakkopasanen/AutoEq) / autoeq.app.
2. Export **ParametricEQ.txt** (Equalizer APO format).
3. EasyEffects → Equalizer → **APO** / Load APO Preset → select file.
4. Confirm preamp/negative gain imported to avoid clipping.
5. Validate with [methodology](../docs/methodology/TEST_PROTOCOL.md) on Music Fidelity + Fatigue.

## How to convert (future tooling)

Planned under `scripts/` (not written yet):

| Step | Action |
|------|--------|
| Parse | Read APO `Preamp` + `Filter N` lines (PK/LSC/HSC/…) |
| Map | Convert to EasyEffects equalizer band objects / or keep APO mode |
| Emit | Optional JSON fragment or full preset overlay |
| Validate | `scripts/validate.sh` + datasheet update |

EasyEffects already understands APO text for Equalizer — conversion may be unnecessary for humans; automation helps batch headphone packs.

## How to validate

| Check | Pass criteria |
|-------|---------------|
| Preamp | No persistent limiter GR on quiet content |
| Tonal | Less “wrong” than stock HP on pink/music refs |
| Stacking | Content preset still meets category primary metrics |
| Regression | A/B vs uncorrected HP |

## Non-goals (now)

- Shipping large measurement databases
- Claiming medical/hearing accuracy
- Replacing oratory1990 / Crinacle communities
