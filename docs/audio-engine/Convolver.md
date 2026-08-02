# Convolver

Part of the [audio engine handbook](README.md).

## Function

Convolution with impulse responses: reverb, headphone HRTF, speaker correction, HeSuVi-like matrices.

## Advantages

- Best path to virtualization / correction on Linux
- Transparent when IR is high quality

## Disadvantages

- CPU + latency
- Bad IRs sound worse than no processing
- Legal/quality issues with random IR packs

## When to use

Future HRTF / AutoEQ-adjacent correction; cinematic room flavors.

## When to avoid

Low-latency competitive gaming until measured safe; untrusted IR sources.

## Practical examples

- Keep wet/dry and IR gain conservative
- Store vetted IRs under `impulse-responses/`

## See also

- [Feature matrix](../../research/FEATURE_MATRIX.md)
- [Test protocol](../methodology/TEST_PROTOCOL.md)
