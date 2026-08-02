# Hardware bank

Catalog of test devices. Add rows as devices are actually tested — do not invent measured results.

| Category | Path |
|----------|------|
| Notebook | [notebook/](notebook/) |
| Desktop | [desktop/](desktop/) |
| USB DAC | [usb-dac/](usb-dac/) |
| Realtek | [realtek/](realtek/) |
| Creative | [creative/](creative/) |
| Headphones | [headphones/](headphones/) |
| IEM | [iem/](iem/) |
| Speakers 2.0 | [speakers-2.0/](speakers-2.0/) |
| Speakers 2.1 | [speakers-2.1/](speakers-2.1/) |
| Soundbar | [soundbar/](soundbar/) |
| Bluetooth | [bluetooth/](bluetooth/) |

Template: [DEVICE_TEMPLATE.md](DEVICE_TEMPLATE.md)

## Priority matrix for v1.x validation

| Priority | Device class | Why |
|----------|--------------|-----|
| P0 | Over-ear closed headphones | Most common EE use case |
| P0 | Notebook Realtek speakers | FxSound/Dolby migrant scenario |
| P1 | IEMs | AutoEQ-sensitive |
| P1 | USB DAC + headphones | Clean chain reference |
| P2 | 2.0 / 2.1 desktop speakers | Stereo Tools / bass behaviour |
| P3 | Soundbar / Bluetooth | Codec + DSP stacking risks |
