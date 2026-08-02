# Audio engine handbook

Engineering notes for the EasyEffects plugins used (or planned) in this repository.

| Document | Plugin |
|----------|--------|
| [Equalizer.md](Equalizer.md) | Equalizer |
| [Compressor.md](Compressor.md) | Compressor |
| [Limiter.md](Limiter.md) | Limiter |
| [BassEnhancer.md](BassEnhancer.md) | Bass Enhancer |
| [Exciter.md](Exciter.md) | Exciter |
| [StereoTools.md](StereoTools.md) | Stereo Tools |
| [AutoGain.md](AutoGain.md) | Autogain |
| [Convolver.md](Convolver.md) | Convolver |
| [MultibandCompressor.md](MultibandCompressor.md) | Multiband Compressor |

## Gain staging philosophy

1. Fix tone with EQ before heavy dynamics when possible.
2. Enhancers (bass/exciter/width) before peak limiting.
3. Autogain early or mid-chain; **always** end with limiter on loud presets.
4. Prefer two honest presets (light/heavy) over one extreme preset.
