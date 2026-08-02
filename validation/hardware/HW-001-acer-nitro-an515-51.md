# HW-001 — Acer Nitro AN515-51

| Field | Value |
|-------|-------|
| Manufacturer | Acer |
| Model | Nitro AN515-51 |
| Type | Notebook |
| Codec | Realtek ALC255 (HDA Intel PCH) |
| Additional audio | NVIDIA GP107GL HDMI (LG ULTRAWIDE) |
| Default PipeWire sink | `alsa_output.pci-0000_00_1f.3.analog-stereo` |
| Sample spec | float32le 2ch 48000Hz |
| PipeWire | 1.0.5 (pipewire-pulse 15.0.0) |
| EasyEffects | Flatpak com.github.wwmm.easyeffects **8.2.8** |
| Kernel | 7.0.0-28-generic |
| Distribution | Linux Mint 22.3 (Zena) |
| Chassis | laptop |
| Firmware | V1.22 (2019-03-15) |
| Tester | siviero |
| Date added | 2026-08-02 |

## Notes

- OEM laptop speakers / combo jack path via ALC255.
- EasyEffects 8 stores presets under Flatpak **XDG data**: `~/.var/app/com.github.wwmm.easyeffects/data/easyeffects/output/`.
- Campaign VC-2026-08 primary device.
