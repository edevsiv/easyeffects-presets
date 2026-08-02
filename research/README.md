# Research laboratory

This directory is the **engineering research lab** for EasyEffects Presets Premium.

We reverse-map commercial / OEM audio suites to open EasyEffects + PipeWire building blocks, then feed findings into preset design.

## Index

| Area | Path | Focus |
|------|------|-------|
| Feature matrix | [FEATURE_MATRIX.md](FEATURE_MATRIX.md) | Capability map vs EasyEffects |
| FxSound | [fxsound/](fxsound/) | Open-source Windows enhancer DSP |
| Dolby Audio | [dolby/](dolby/) | PC Entertainment Experience / Volume / Virtualizer |
| DTS:X / Sound Unbound | [dtsx/](dtsx/) | Spatial / Headphone:X |
| SteelSeries Sonar | [steelseries-sonar/](steelseries-sonar/) | Gaming EQ + channel mix |
| Peace + Equalizer APO | [peace-equalizer/](peace-equalizer/) | System-wide Windows EQ |
| Realtek Audio Console | [realtek/](realtek/) | OEM codec control panel |
| Waves MaxxAudio | [waves-maxxaudio/](waves-maxxaudio/) | OEM loudness / bass / dialog |
| Nahimic | [nahimic/](nahimic/) | Gaming spatial / immersion |
| EasyEffects | [easyeffects/](easyeffects/) | Plugin inventory & architecture |
| PipeWire | [pipewire/](pipewire/) | Graph, quantum, latency research |
| Linux audio stack | [linux-audio/](linux-audio/) | LV2, JACK, PipeWire ecosystem |

## Related project docs

- [../docs/audio-engine/](../docs/audio-engine/) — plugin engineering notes
- [../docs/methodology/TEST_PROTOCOL.md](../docs/methodology/TEST_PROTOCOL.md) — official listening protocol
- [../benchmark/](../benchmark/) — comparative benchmark
- [../AUDIO_ROADMAP.md](../AUDIO_ROADMAP.md) — technical roadmap to v3.0
- [../references/](../references/) — reference content library

## Research principles

1. Prefer **public documentation**, white papers, and open source over marketing claims.
2. Map every commercial feature to an **EasyEffects-equivalent** (exact, approximate, or gap).
3. Document **limitations** — Linux cannot clone proprietary HRTF databases or OEM speaker tunings bit-identically.
4. Feed results into presets only after the [test protocol](../docs/methodology/TEST_PROTOCOL.md).
