# Equalizer

Part of the [audio engine handbook](README.md).

## Function

Multi-band tonal filter (IIR/FIR/FFT/SPM modes in EasyEffects). Shapes magnitude response across frequency.

## Advantages

- Most powerful “character” control
- Can approximate AutoEQ / device correction
- Split L/R possible for asymmetric headphones

## Disadvantages

- Easy to create harshness or thinness
- High band counts + FFT modes cost CPU
- Incorrect preamp causes clipping before limiter

## When to use

Always as the primary tonal tool for music, cinema presence, and gaming cue emphasis.

## When to avoid

Avoid extreme narrow boosts for long sessions; avoid fixing dynamics problems with EQ alone.

## Practical examples

- Dialog: gentle +2 to +4 dB around 2–4 kHz
- Footsteps: controlled presence 3–6 kHz without hiss
- Laptop speakers: cut 200–400 Hz mud, careful bass shelf

## See also

- [Feature matrix](../../research/FEATURE_MATRIX.md)
- [Test protocol](../methodology/TEST_PROTOCOL.md)
