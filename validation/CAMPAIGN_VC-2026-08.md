# Campaign VC-2026-08 — First official validation

| Field | Value |
|-------|-------|
| ID | VC-2026-08 |
| Start | 2026-08-02 |
| Host | Acer Nitro AN515-51 (siviero) |
| EasyEffects | Flatpak **8.2.8** |
| PipeWire | 1.0.5 @ 48 kHz stereo |
| Kernel | 7.0.0-28-generic |
| Distro | Linux Mint 22.3 |

## Objectives

1. Install and UI-load every project preset on real hardware.
2. Capture EasyEffects screenshots (main / chain / EQ / compressor when present).
3. Record compatibility defects with evidence.
4. Apply documented schema fixes for EE8.
5. Seed metric scorecards (design-audit + ui-load).
6. Prepare release candidate materials.

## Content matrix (required categories)

| Content class | Used in campaign | Notes |
|---------------|------------------|-------|
| Filmes | Yes (mpv playing during session) | Background playback present |
| Música | Planned / references ready | Full A/B pending |
| Jogos | Pending human session | Protocol ready |
| Speech | Pending | voice presets targeted |
| YouTube | Pending | |
| Streaming | Pending | |

## Outcomes (engineering)

| Finding | Evidence | Action |
|---------|----------|--------|
| `bass_enhancer.scope="Mono"` rejected | UI error banner | Migrated to numeric scope |
| `bass_enhancer.blend` 0–1 scale rejected | UI error | Migrated to percent-like values |
| Legacy `limiter.limit` + `stereo-link="Average"` rejected | UI error banner | Migrated to EE8 `threshold` + numeric stereo-link |
| Screenshots captured for all 11 presets | `validation/screenshots/` | Replaced SVG placeholders in README paths with PNG |

## Status

Campaign **open**. UI/compat track largely complete; subjective listening track in progress.
