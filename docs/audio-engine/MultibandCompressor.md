# Multiband Compressor

Part of the [audio engine handbook](README.md).

## Function

Splits spectrum into bands and compresses independently — density without full-band pumping.

## Advantages

- “Commercial loudness” character
- Controls boom vs harshness separately
- Strong FxSound Dynamic Boost / maximizer analogue when paired with limiter

## Disadvantages

- Complex to tune
- Can sound squashed or disconnected across bands
- CPU heavier

## When to use

`*-02` cinematic/enhancer presets; problematic dynamic soundtracks.

## When to avoid

Minimal audiophile chains; already limited masters.

## Practical examples

- Compress low band for boom control
- Gentle highs to tame harshness without dulling

## See also

- [Feature matrix](../../research/FEATURE_MATRIX.md)
- [Test protocol](../methodology/TEST_PROTOCOL.md)
