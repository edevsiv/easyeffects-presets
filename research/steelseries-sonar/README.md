# Research: SteelSeries Sonar

**Sources:** [steelseries.com/gg/sonar](https://steelseries.com/gg/sonar), Sonar support docs, streaming mode docs.

## Summary

Sonar (inside SteelSeries GG) is a **gaming/streaming audio suite**: per-channel mix (Game, Chat, Media, Aux, Mic), parametric EQ per channel, spatial modes, ChatMix, and app routing.

## Features relevant to presets

| Feature | Description |
|---------|-------------|
| Parametric EQ | Competitive footprints, immersive movie presets |
| Channel separation | Independent processing for game vs chat |
| Spatial audio | 360° virtualization on arbitrary headsets |
| Mic chain | Gate, noise suppression, EQ (input path) |
| Smart volume / stabilizers | Automatic level behaviors |

## Strengths

- Excellent **workflow** for gamers/streamers
- Per-app routing mental model
- Competitive EQ culture (footstep-focused curves)

## Limitations

- Windows-centric; vendor ecosystem
- Spatial quality depends on proprietary renderer
- Easy to stack Engine + Sonar conflicting profiles

## EasyEffects equivalence

| Sonar | EasyEffects / PipeWire |
|-------|------------------------|
| Per-channel EQ | Multiple EasyEffects instances / per-app effects |
| Game EQ presets | `gaming-01` / `gaming-02` category |
| Chat clarity | Input effects + output voice presets |
| Spatial | Convolver / Stereo Tools (partial) |
| App routing | PipeWire / Helvum / EasyEffects app list |

## Design implications

1. Competitive presets should emphasize **2–6 kHz cues** without destroying tonal balance.
2. Immersive presets may widen stereo and lift bass carefully.
3. Document that Linux “ChatMix” is a **routing** problem first, DSP second.
