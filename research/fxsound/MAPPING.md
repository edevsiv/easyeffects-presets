# FxSound → EasyEffects complete mapping

Companion to [README.md](README.md).

## Knob map

| FxSound control | Perceptual goal | EasyEffects equivalent | Notes |
|-----------------|-----------------|------------------------|-------|
| **Fidelity** | Clarity / harmonic brilliance | `exciter` (+ optional Crystalizer) | Map intensity → `amount` / `harmonics`; start low on bright IEMs |
| **Ambience** | Room / bloom | `reverb` (wet very low) or `convolver` room IR | Easy to smear transients; classical preset uses tiny wet |
| **Surround** | Stage width | `stereo_tools` (`stereo-base`, side level) | Extreme width collapses dialog center |
| **Dynamic Boost** | Perceived loudness + density | `autogain` + `multiband_compressor` + `limiter` | Closest “stack”, not identical adaptive curve |
| **Bass** | Low-end punch / extension | `bass_enhancer` | Harmonic bass ≈ MaxxBass family; always limit after |
| **EQ** | Tonal shape | `equalizer` | Prefer measured targets later (AutoEQ) |

## Suggested translation starting points

| FxSound slider feel | Exciter amount | Bass amount | Stereo-base (EE scale in our `*-02`) | Autogain target |
|---------------------|----------------|-------------|--------------------------------------|-----------------|
| Subtle | 4–8 | 4–8 | 0.1–5 | −23 to −20 |
| Medium | 8–12 | 8–14 | 5–10 | −20 to −18 |
| Aggressive (Ultimate) | 12–20 | 14–20 | 10–15 | −18 |

Reference implementation in-repo: [`fxsound-ultimate-02`](../../presets/experimental/fxsound-ultimate-02.json).

## Pipeline alignment

```text
FxSound:     Capture → DfxDsp(effects+EQ) → Device
EasyEffects: App → [Autogain→MB→EQ→Exciter→Bass→Stereo→Limiter] → Device
```

Order rationale: level → density → tone → harmonics → width → safety.

## Limitations vs FxSound

1. No virtual driver UX — PipeWire/EasyEffects app selection instead.
2. DfxDsp internals ≠ LV2 plugins; matching is perceptual/engineering, not bitwise.
3. FxSound presets (`.fac`) are not importable; rebuild via this map.
