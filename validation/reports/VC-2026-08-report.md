# Report — VC-2026-08

## Executive summary

First official validation campaign executed on **HW-001 (Acer Nitro AN515-51)** with **EasyEffects Flatpak 8.2.8**.

- 11/11 presets UI-loaded and screenshot-captured
- EE8 compatibility defects found and fixed for legacy `*-01` bass/limiter schemas
- All presets sealed **Beta** (or Experimental for FxSound showcase)
- Subjective multi-content A/B still required for **Validated** seals

## Hardware

See [../hardware/HW-001-acer-nitro-an515-51.md](../hardware/HW-001-acer-nitro-an515-51.md).

## Score summary

Mean overall (design-audit+ui-load): **3.27**

Details: [../results/VC-2026-08-scores.md](../results/VC-2026-08-scores.md)

## Compatibility defects closed

1. Bass Enhancer `scope`/`blend` legacy types
2. Limiter `limit` + string `stereo-link`

Documented under `measurements/version-history/*ee8*`.

## Remaining risks

- Some compressor tab captures may require manual click verification
- Limiter error banners observed mid-campaign until schema migration completed — re-verify visually after each EE upgrade
- No full subjective A/B vs Flat/FxSound/Dolby yet

## Recommendation

Ship **v1.0.0-rc1** (release candidate). Defer **v1.0.0 Stable** until ≥1 filled subjective log per category.
