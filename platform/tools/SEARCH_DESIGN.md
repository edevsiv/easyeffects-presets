# Search mechanism design

## User input

```text
Hardware (class and/or HW-ID and/or chipset)
        ↓
Optional: content intent (movie / music / gaming / voice)
        ↓
Optional: constraints (low latency, headphones, BT)
```

## Outputs

| Output | Source |
|--------|--------|
| Recommended profile(s) | [recommend-by-hardware.md](recommend-by-hardware.md) + `database/profiles.json` |
| Calibration playbook | `platform/calibration/` → root `calibration/` |
| AutoEQ guidance | `autoeq/` + `platform/dsp/autoeq.md` |
| Observations | Hardware scorecard |

## Implementation phases

| Phase | Delivery |
|-------|----------|
| Now | Markdown matrices + manual lookup |
| v2 | CLI reading `profiles.json` + scorecards |
| v3 | Website search (`docs/site` → static search index) |
| v4+ | Optional online service (out of scope until governance OK) |

## Ranking heuristics (draft)

1. Prefer Validated/Stable seals over Experimental
2. Prefer `*-01` when Fatigue risk or unknown FR
3. Prefer profiles with matching `validated_hardware`
4. Deprioritize heavy convolvers on BT / competitive gaming
