# Hardware calibration database (platform index)

Authoritative playbooks remain under repository root [`calibration/`](../../calibration/).
This folder indexes them for the platform search/recommendation UX.

| Class | Playbook |
|-------|----------|
| Notebook | [../../calibration/Notebook/](../../calibration/Notebook/) |
| Realtek | [../../calibration/Realtek/](../../calibration/Realtek/) |
| USB DAC | [../../calibration/USB-DAC/](../../calibration/USB-DAC/) |
| Bluetooth | [../../calibration/Bluetooth/](../../calibration/Bluetooth/) |
| Gaming headset | [../../calibration/Gaming-Headset/](../../calibration/Gaming-Headset/) |
| Speakers 2.0 | [../../calibration/2.0-Speakers/](../../calibration/2.0-Speakers/) |
| Speakers 2.1 | [../../calibration/2.1-Speakers/](../../calibration/2.1-Speakers/) |

## Workflow

1. Identify hardware class (`platform/hardware/`)
2. Open matching playbook
3. Apply recommended profile from search ([../tools/SEARCH_DESIGN.md](../tools/SEARCH_DESIGN.md))
4. Optional AutoEQ / Convolver layers
5. File listening session under `validation/campaigns/`
