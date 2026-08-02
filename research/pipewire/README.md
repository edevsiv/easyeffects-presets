# Research: PipeWire for DSP presets

Companion to [../../docs/PIPEWIRE.md](../../docs/PIPEWIRE.md).

## Why it matters

Every EasyEffects preset runs inside the PipeWire graph. Quantum, rate, and CPU contention change whether a heavy multiband chain is usable.

## Research findings (operational)

| Topic | Guidance |
|-------|----------|
| Rate | 48 kHz default is fine for consumer presets |
| Quantum | 1024 desktop; 256–512 competitive if stable |
| Xruns | First response: raise quantum, simplify chain |
| Flatpak | Host PipeWire; verify app appearance in EE |
| Measuring | `pw-top`, EasyEffects latency labels |

## Interaction with commercial suites

Windows enhancers often use WASAPI exclusive/virtual devices. PipeWire’s graph model is closer to JACK: **explicit nodes** and flexible routing, which is an advantage for per-app processing once documented well.
