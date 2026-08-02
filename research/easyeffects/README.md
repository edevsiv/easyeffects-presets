# Research: EasyEffects architecture

**Sources:** [wwmm/easyeffects](https://github.com/wwmm/easyeffects), [Easy Effects Manual](https://wwmm.github.io/easyeffects/), plugins properties database.

## Role in this project

EasyEffects is our **DSP host**. Presets are JSON graphs of LV2/internal effects applied to PipeWire streams (output and/or input).

## Effect inventory (selected)

| Plugin | Primary use in this repo |
|--------|--------------------------|
| Equalizer | Tonal design, device/content EQ |
| Bass Enhancer | Harmonic/sub enhancement |
| Exciter | Harmonic brilliance / “fidelity” |
| Stereo Tools | Width, balance, soft mute sides |
| Compressor | Glue / dialog leveling |
| Multiband Compressor | Loudness-style density |
| Autogain | LUFS targeting |
| Limiter / Maximizer | Peak safety |
| Gate / De-esser | Speech cleanup (playback or input) |
| Reverb | Classical / ambience spice |
| Convolver | HRTF / speaker correction (future) |
| Loudness | Equal-loudness contour compensation |
| Crystalizer | Transient emphasis (use sparingly) |
| Crossfeed | Headphone speaker-like blend |
| Crosstalk Canceller | Speaker virtualization aid |

## Preset JSON shape

```json
{
  "output": {
    "plugins_order": ["equalizer#0", "limiter#0"],
    "equalizer#0": { },
    "limiter#0": { },
    "blocklist": []
  }
}
```

Order is user-controlled and critical for gain staging.

## Recommended chain archetypes

| Archetype | Order sketch |
|-----------|--------------|
| Minimal music | EQ → Exciter → Stereo Tools → Limiter |
| Cinema dense | Autogain → Multiband → EQ → Exciter → Bass → Stereo → Limiter |
| Speech | EQ → Gate → Comp → De-esser → Limiter |
| Competitive game | EQ → Bass (light) → Stereo → Comp → Limiter |

See [../../docs/audio-engine/](../../docs/audio-engine/) for plugin-level engineering notes.
