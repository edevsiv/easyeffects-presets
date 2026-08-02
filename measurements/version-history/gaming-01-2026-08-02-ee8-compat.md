# gaming-01 — 2026-08-02 EE8 compatibility fix

## Why it changed

EasyEffects 8.2.8 rejects bass_enhancer scope string "Mono" and 0–1 blend; migrate to numeric scope/blend.

Observed UI error during FASE 04 capture campaign:
`Preset not loaded correctly. Amplificador dos Graves: One or more parameters have a wrong format.`

## What changed

| Parameter | Before | After |
|-----------|--------|-------|
| scope | 'Mono' | 100.0 |
| blend | 0.25 | 25.0 |

## Expected result

Preset loads cleanly on EasyEffects 8.2.8 Flatpak without bass enhancer format errors; bass processing engages.

## Benchmark

Reload preset in EE UI; confirm red error bar absent; compare meters vs previous.

## Status

Applied in FASE 04 validation campaign (objective UI evidence).
