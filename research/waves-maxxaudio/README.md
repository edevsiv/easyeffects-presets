# Research: Waves MaxxAudio

**Sources:** Waves MaxxAudio OEM marketing, MaxxBass / MaxxVoice / MaxxStereo literature.

## Summary

Waves MaxxAudio is an OEM suite bundling psychoacoustic enhancers widely used on laptops:

| Module | Intent |
|--------|--------|
| **MaxxBass** | Perceived bass extension on small speakers via harmonics |
| **MaxxVoice** / dialog | Speech intelligibility |
| **MaxxTreble** | Air / clarity |
| **MaxxStereo** / Space | Image width |
| **MaxxVolume** | Loudness without obvious clipping |
| EQ | User tonal control |

## EasyEffects equivalence

| Maxx module | EasyEffects |
|-------------|-------------|
| MaxxBass | `bass_enhancer` (harmonics) — closest conceptual match |
| MaxxVoice | Presence EQ + de-esser + mild compression |
| MaxxStereo | `stereo_tools` |
| MaxxVolume | `autogain` + `limiter`/`maximizer` |
| Treble | High shelf / exciter |

## Notes

MaxxBass is historically important: **harmonic bass generation** rather than only shelving EQ. Our Bass Enhancer usage in cinema/gaming/experimental presets follows that idea—with limiter mandatory.
