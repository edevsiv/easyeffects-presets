# Installation guide

This document covers installing **EasyEffects**, required plugins, and importing presets from this repository.

## Requirements

| Component | Notes |
|-----------|--------|
| Linux | Any modern distro with PipeWire |
| [PipeWire](https://pipewire.org/) | Recommended audio server (+ WirePlumber) |
| [EasyEffects](https://github.com/wwmm/easyeffects) | v7+ recommended |
| LV2 plugins | Bundled with most EasyEffects packages; LSP / Calf often needed |

EasyEffects **does not** replace PipeWire — it inserts itself as a filter on playback (and optionally capture) streams.

## Install EasyEffects

### APT (Debian / Ubuntu / derivatives)

```bash
sudo apt update
sudo apt install easyeffects
```

Optional plugin packages (names vary by distro):

```bash
sudo apt install lsp-plugins calf-plugins zam-plugins
```

On Ubuntu, a [PPA](https://github.com/wwmm/easyeffects#installation) may provide newer EasyEffects builds than the default archive.

### Fedora

```bash
sudo dnf install easyeffects
```

### Arch Linux

```bash
sudo pacman -S easyeffects
```

### Flatpak (universal)

```bash
flatpak install flathub com.github.wwmm.easyeffects
```

Flatpak isolates configuration under `~/.var/app/com.github.wwmm.easyeffects/`.

## Preset directories

Exact paths depend on install method and EasyEffects version.

| Install | Typical output presets path |
|---------|-----------------------------|
| Native (newer / EE8) | `~/.local/share/easyeffects/output/` |
| Native (older) | `~/.config/easyeffects/output/` |
| Flatpak (EE8 data) | `~/.var/app/com.github.wwmm.easyeffects/data/easyeffects/output/` |
| Flatpak (legacy config) | `~/.var/app/com.github.wwmm.easyeffects/config/easyeffects/output/` |

Related folders you may also see: `input/`, `irs/`, `rnnoise/`, `autoload/`.

Community note from upstream: newer EasyEffects builds prefer **XDG data** (`~/.local/share/easyeffects`) while Flatpak users often still find presets under the Flatpak **config** tree. If unsure, create a dummy preset in the UI and locate the new `.json` file.

## Import presets

### Option A — installer script (recommended)

```bash
git clone https://github.com/edevsiv/easyeffects-presets.git
cd easyeffects-presets
chmod +x scripts/install.sh
./scripts/install.sh
```

Flags:

```bash
./scripts/install.sh --flatpak
./scripts/install.sh --native
./scripts/install.sh --dry-run
```

### Option B — EasyEffects UI

1. Open EasyEffects
2. Go to **Presets**
3. Use **Import Preset** / load file
4. Select a JSON from `presets/<category>/`

### Option C — manual copy

```bash
# Example: native XDG data path
mkdir -p ~/.local/share/easyeffects/output
cp presets/movie/*.json ~/.local/share/easyeffects/output/
```

Restart EasyEffects or reload the presets list after copying.

## Version differences

| Topic | Older EasyEffects | Newer EasyEffects |
|-------|-------------------|-------------------|
| History | Fork of PulseEffects | PipeWire-native effects host |
| Preset format | Evolved since 6.x | Current `output` / `plugins_order` JSON |
| Storage | Often `~/.config/easyeffects` | Often `~/.local/share/easyeffects` |
| Flatpak | Sandboxed under `~/.var/app/...` | Same idea; verify with a saved preset |

PulseEffects (PulseAudio-era) presets are **not** guaranteed to load. Upstream documents converters on the [Community Presets](https://github.com/wwmm/easyeffects/wiki/Community-Presets) wiki.

## Verify installation

1. Play audio (browser, player, or game)
2. Confirm EasyEffects shows the application in the effects pipeline
3. Enable a preset (e.g. `music-hd-01`)
4. Watch meters move and listen for EQ / dynamics changes

## Next steps

- [PIPEWIRE.md](PIPEWIRE.md) — buffer, latency, sample rate
- [MPV.md](MPV.md) — film playback and downmix tips
- [../presets/README.md](../presets/README.md) — preset catalog
