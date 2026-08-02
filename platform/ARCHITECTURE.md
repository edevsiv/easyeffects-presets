# Platform architecture

## Layers

```text
┌─────────────────────────────────────────────────────────────┐
│  Community  ·  Issues / PRs / Listening / Hardware reports  │
├─────────────────────────────────────────────────────────────┤
│  Site IA (docs/site)  ·  Search UX  ·  Downloads            │
├─────────────────────────────────────────────────────────────┤
│  Tools  ·  recommend-by-hardware  ·  AutoEQ recommend.py    │
├─────────────────────────────────────────────────────────────┤
│  Databases                                                   │
│   audio-profiles  ·  hardware  ·  calibration  ·  IR catalog │
├─────────────────────────────────────────────────────────────┤
│  Knowledge                                                   │
│   platform/dsp  ·  docs/audio-engine  ·  research/           │
├─────────────────────────────────────────────────────────────┤
│  Artifacts                                                   │
│   presets/*.json  ·  validation evidence  ·  measurements    │
├─────────────────────────────────────────────────────────────┤
│  Runtime                                                     │
│   Linux · PipeWire · EasyEffects · LV2 plugins               │
└─────────────────────────────────────────────────────────────┘
```

## Data flow (user journey)

```text
Hardware identity
        ↓
Hardware scorecard + calibration playbook
        ↓
Search / recommendation (tools)
        ↓
Audio profile card → preset JSON
        ↓
Optional AutoEQ / Convolver layers
        ↓
Listening session → certification gates
```

## Profile identity

Canonical ID = preset stem (e.g. `cinema-01`).  
JSON path = `presets/<category>/<id>.json`.  
Platform card = `platform/audio-profiles/<id>.md`.  
Validation dossier = `validation/profiles/<id>.md`.

## Versioning

| Layer | Version field |
|-------|----------------|
| Preset JSON | file content + HISTORY / datasheet |
| Profile card | `profile_version` in frontmatter |
| Platform docs | repository semver / release channel |
| Certification seal | `validation/STATUS.md` |

## Extension points (future)

1. Machine-readable `database/profiles.json` consumed by a website
2. Hardware → profile recommender CLI under `platform/tools/`
3. Optional SQLite/JSON export for offline apps
4. Convolver IR packs as separate data releases
