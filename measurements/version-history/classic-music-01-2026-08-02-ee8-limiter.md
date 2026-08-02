# classic-music-01 — 2026-08-02 EE8 limiter schema migration

## Why it changed

EasyEffects 8.2.8 Flatpak rejected legacy limiter fields during FASE 04 UI validation:
`Preset not loaded correctly. Limitador: One or more parameters have a wrong format.`

Legacy presets used `limit` + string `stereo-link` (e.g. `"Average"`). EE8 expects `threshold` + numeric `stereo-link` and the modern ALR/sidechain key set.

## What changed

| Field | Before | After |
|-------|--------|-------|
| stereo-link | 'Average' | 100.0 |
| limit | -1.5 | (removed) |
| threshold | None | -1.5 |

Limiter block migrated to EE8 schema while preserving ceiling/attack/release intent.

## Expected result

Clean preset load without red error banner; limiter engages on peaks.

## Evidence

UI screenshots from Acer Nitro AN515-51 campaign (EasyEffects Flatpak 8.2.8).

## Status

Applied in FASE 04.
