# AutoEQ — future integration plan

## Today (FASE 06)

| Capability | Status |
|------------|--------|
| APO parser | `convert_apo_to_bands.py` |
| Markdown recommendations | `recommend.py` |
| Auto-edit presets | **Forbidden** |
| Website search hook | Designed in `platform/tools/SEARCH_DESIGN.md` |

## Target architecture

```text
Headphone model → AutoEQ ParametricEQ.txt
        ↓
recommend.py / future CLI
        ↓
User imports APO into Equalizer
        ↓
Content profile (prefer no-eq variant when available)
        ↓
Listening form
```

## Planned milestones

| Milestone | Delivery |
|-----------|----------|
| v2.0 | Documented no-eq content variants (still manual) |
| v2.1 | CLI: `ee-platform recommend --headphones …` |
| v3.0 | Optional band merge preview (diff only; user applies) |
| v4.0 | Site search integrates headphone → correction → profile |

## Non-goals

- Shipping copyrighted measurement DBs
- Silent overwrite of user presets
