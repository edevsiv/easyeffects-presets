# Recommend-by-hardware (manual engine)

Lookup table for the search design. **Not certified** — listening campaign pending.

| Hardware input | Recommended profile | Calibration | AutoEQ | Observations |
|----------------|---------------------|-------------|--------|--------------|
| Notebook / ALC255 (HW-001) | `cinema-01` or `gaming-01` | Notebook + Realtek | Optional if using headphones | Speakers uneven; avoid OEM DSP |
| Unknown headphones | `music-hd-01` | Headphones class | **Yes** — import APO first | Do not stack smile EQ |
| Gaming headset | `gaming-01` | Gaming-Headset | If measured | Competitive: keep chain light |
| USB DAC | `music-hd-01` / `classic-music-01` | USB-DAC | If headphones | Let DAC handle loudness |
| Bluetooth sink | `voice-boost-01` / light `*-01` | Bluetooth | Rarely | Latency + remote DSP risk |
| Speakers 2.0 | `music-hd-01` | 2.0-Speakers | No | Check harsh treble |
| Speakers 2.1 | `cinema-01` then careful `*-02` | 2.1-Speakers | No | Sub integration |
| HDMI (AMD/Intel/NVIDIA) | content `*-01` | (playbook TBD) | No | Ensure PCM, not bitstream |

Machine-readable future: consume [../database/profiles.json](../database/profiles.json).
