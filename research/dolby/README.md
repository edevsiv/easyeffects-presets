# Research: Dolby Audio (PC)

**Sources:** Dolby Advanced Audio v2 / Home Theater v4 product pages, [PCEE v4 white paper](https://professional.dolby.com/siteassets/pdfs/dolby-pc-entertainment-experience-v4-white-paper.pdf), Dolby Volume tech paper.

## Summary

Dolby’s PC Entertainment Experience suites target **laptop speakers and headphones**: consistent loudness, distortion-free maximization, dialog intelligibility, and virtual surround via **HRTF**-based rendering.

## Key technologies

### Voice / dialog enhancement

- Presence shaping and content-aware EQ (suite-dependent naming: Intelligent EQ / dialog clarity families)
- Goal: speech remains intelligible when effects and music are loud

### Volume Leveler

- Maintains a **preferred loudness** across apps and content
- Psychoacoustic leveling (related to Dolby Volume lineage)

### Volume Maximizer

- Boosts level (marketing often cites up to ~12 dB)
- Uses **look-ahead limiting** + multiband control to avoid clipping/pumping

### Virtual Surround

- Surround Decoder: stereo→5.1 / 5.1→7.1 upmix paths
- Surround Virtualizer: HRTF rendering to headphones or crosstalk-managed speakers

### Dynamic Range Compression

- Night / quiet listening modes reduce peaks while lifting soft dialog
- Distinct from pure peak limiting

### Equalizer / Audio Optimizer / Regulator

- Graphic EQ for taste
- Optimizer/Regulator families protect small speakers from overdrive

## Strengths

- Mature psychoacoustic design
- Excellent consistency across heterogeneous content
- Strong OEM integration (device-specific speaker protection)

## Limitations

- Closed source; OEM-locked features
- Difficult to isolate exact algorithm parameters
- Linux has no first-party Dolby PC Entertainment stack

## EasyEffects equivalence

| Dolby feature | EasyEffects approach | Fidelity |
|---------------|----------------------|----------|
| Voice enhancement | EQ 2–4 kHz + de-esser + gate | Approximate |
| Volume Leveler | `autogain` (LUFS targets via libebur128) | Good approx. |
| Volume Maximizer | `maximizer` / `limiter` | Approximate |
| DRC | `compressor` / `multiband_compressor` | Approximate |
| Virtualizer | `convolver` HRTF / crosstalk canceller | Partial — no Dolby HRTF DB |
| Graphic EQ | `equalizer` | Strong |

## Design implications for cinema presets

1. Prefer **Autogain → Multiband → EQ → Limiter** for streaming consistency (`cinema-02`).
2. Keep a lighter dialog path (`cinema-01`, `voice-boost-01`) without heavy virtualization.
3. Never claim “Dolby equivalent” — claim “Dolby-inspired leveling goals”.
