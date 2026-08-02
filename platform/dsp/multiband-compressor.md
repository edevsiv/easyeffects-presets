# Why use a multiband compressor

## Problem

A single-band compressor reacts to the whole spectrum. Loud bass can duck vocals;
sibilance can pump the mix.

## Engineering intent

Split the spectrum so **bass**, **mids**, and **highs** have independent thresholds.
In cinema/gaming `*-02` chains this:

1. Controls dialogue vs LFE competition
2. Increases apparent loudness without a single broadband squash
3. Lets exciters/bass enhancers work on a more managed signal

## When to use

- Dense movie / music enhancer stacks
- Highly dynamic game mixes with explosions + speech
- After Autogain when levels vary wildly

## When not to use

- Competitive gaming needing maximum transient honesty
- Critical classical listening (`classic-music-01` avoids heavy MBC)
- Low-CPU / low-latency targets

## See also

[docs/audio-engine/MultibandCompressor.md](../../docs/audio-engine/MultibandCompressor.md)
