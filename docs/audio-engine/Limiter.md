# Limiter

Part of the [audio engine handbook](README.md).

## Function

Brick-wall (or near brick-wall) peak control with ceiling/lookahead variants depending on backend.

## Advantages

- Safety net for enhancers and autogain
- Enables louder presets without digital overs
- Mandatory for bass/exciter chains

## Disadvantages

- Overuse causes squashed, fatiguing sound
- Lookahead adds latency
- Can encode “always loud” fatigue

## When to use

End of nearly every output preset in this repository.

## When to avoid

As the *only* loudness tool without proper gain structure upstream.

## Practical examples

- Ceiling slightly below 0 dBFS
- After Autogain/Multiband in cinema-02 style chains

## See also

- [Feature matrix](../../research/FEATURE_MATRIX.md)
- [Test protocol](../methodology/TEST_PROTOCOL.md)
