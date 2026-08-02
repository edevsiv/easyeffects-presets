# Audio profile schema

Every platform profile card and `profiles.json` entry SHOULD expose:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Stable kebab-case ID (`cinema-01`) |
| `category` | enum | `movie` · `music` · `gaming` · `voice` · `experimental` |
| `objective` | string | One-sentence listening goal |
| `version` | string | Profile card / datasheet revision (`1.0.0-rc1` class) |
| `recommended_hardware` | string[] | HW class IDs or chipset tags |
| `validated_hardware` | string[] | HW IDs with evidence (UI and/or listening) |
| `plugins` | string[] | EasyEffects plugin keys in chain |
| `pipeline` | string | Ordered DSP pipeline summary |
| `history` | path | Link to HISTORY / version-history |
| `limitations` | string | Known risks / non-goals |
| `compatibility` | object | EE major, PipeWire notes |
| `license` | string | Usually MIT (repo) |
| `seal` | enum | Experimental…Reference |
| `preset_path` | path | Relative path to JSON |

## Lifecycle

```text
draft card → linked JSON → Beta evidence → Validated listening → Stable release
```
