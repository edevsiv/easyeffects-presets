# AutoEQ recommendation — `Example-IEM`

## Summary

Apply headphone correction **before** or **instead of** stacking smile-curve content EQ.

- Suggested preamp: **-6.0 dB** (from APO file)
- Filters parsed: **4**

## How to apply (manual)

1. EasyEffects → Equalizer → **APO** → import the ParametricEQ.txt
2. Confirm meters do not slam the limiter on quiet content
3. Then load a content preset **or** use a future `no-eq` variant

## Interaction warning

Requested content preset: `music-hd-01`

If that preset already boosts bass/treble heavily (`music-hd-*`, `fxsound-*`, `*-02`),
prefer Flat content EQ or reduce enhancer amounts after correction.

## Band table

| # | Type | Fc (Hz) | Gain (dB) | Q |
|--:|------|--------:|----------:|----:|
| 1 | LSC | 105.00 | +2.30 | 0.70 |
| 2 | PK | 200.00 | -2.00 | 1.20 |
| 3 | PK | 3000.00 | +1.50 | 1.40 |
| 4 | HSC | 10000.00 | -1.00 | 0.70 |

## Validation

Run listening form after applying; do not change seal without CERTIFICATION gates.

