# AutoGain

Part of the [audio engine handbook](README.md).

## Function

Automatic loudness leveling toward a target using libebur128-based measurements (momentary/short-term/integrated combinations).

## Advantages

- Cross-app / cross-content consistency (Dolby Leveler analogue)
- Great for mixed playlists and streaming

## Disadvantages

- Can fight intentional dynamics
- May boost noise floors between sections
- Needs limiter downstream

## When to use

Cinema-02, music-02, experimental loudness stacks.

## When to avoid

Album listening where dynamics are artistic intent; competitive gaming if pumping distracts.

## Practical examples

- Target around broadcast-ish loudness (−23 LUFS family) then trim taste
- Geometric mean references for stability

## See also

- [Feature matrix](../../research/FEATURE_MATRIX.md)
- [Test protocol](../methodology/TEST_PROTOCOL.md)
