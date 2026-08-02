# Research: Peace + Equalizer APO

**Sources:** Equalizer APO project docs, Peace GUI community, HeSuVi ecosystem.

## Summary

**Equalizer APO** is a Windows system-wide audio APO (Audio Processing Object). **Peace** is a popular GUI. Together they provide powerful EQ, VST hosting (via extensions), and community configs (including HeSuVi virtual surround).

## Features

- Graphic / parametric EQ with arbitrary complexity
- Preamp / loudness tooling via configs
- Community headphone correction (AutoEQ imports)
- Virtual surround via HeSuVi convolution matrices
- Optional VST chain (compression, limiters, etc.)

## Strengths

- Extremely flexible; near “DAW for the OS”
- Huge community preset/correction library
- Excellent for **measurement-based** headphone EQ

## Limitations

- Windows APO stack only
- Misconfiguration can break audio devices
- Latency/stability depends on plugins used
- No PipeWire-native equivalent as a single product

## EasyEffects equivalence

| Peace / APO | EasyEffects |
|-------------|-------------|
| System EQ | Equalizer plugin |
| AutoEQ curves | Import band gains into Equalizer (manual/scripted) |
| HeSuVi | Convolver + impulse responses |
| VST dynamics | Native compressor/limiter/multiband |
| Global APO | EasyEffects filters PipeWire clients (not identical scope) |

## Design implications

Peace is our **reference for correction culture**. Future `autoeq/` directory will store headphone target notes and conversion guidance, not Windows binaries.
