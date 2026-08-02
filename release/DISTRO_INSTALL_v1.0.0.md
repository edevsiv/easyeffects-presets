# Distro install verification — v1.0.0

Verification scope: **installation paths only** (EasyEffects + preset import). Not full listening matrices per distro.

| Distro | Method verified | Result | Notes |
|--------|-----------------|--------|-------|
| **Linux Mint 22.3** | Flatpak EasyEffects 8.2.8 + `./scripts/install.sh --flatpak` | **PASS** | Reference HW-001; presets land in `~/.var/app/.../data/easyeffects/output/` |
| **Ubuntu** (22.04+/24.04 family) | Docs: `apt install easyeffects` **or** Flatpak; same installer | **PASS (doc + Flatpak path)** | Mint is Ubuntu-family; Flatpak path identical. APT package versions may lag Flatpak. |
| **Fedora** | Docs: `dnf install easyeffects`; Flatpak universal | **PASS (doc)** | Use `./scripts/install.sh --native` for RPM install, or `--flatpak` |
| **Arch Linux** | Docs: `pacman -S easyeffects`; Flatpak universal | **PASS (doc)** | Prefer `--native` → `~/.local/share/easyeffects/output/` on EE8 |

## Commands exercised on reference host (Mint)

```bash
./scripts/validate.sh
./scripts/install.sh --flatpak
flatpak run com.github.wwmm.easyeffects -l cinema-01
```

## Flatpak (all distros)

```bash
flatpak install flathub com.github.wwmm.easyeffects
./scripts/install.sh --flatpak
```

## Native

```bash
./scripts/install.sh --native
```

Full package notes: [docs/INSTALL.md](../docs/INSTALL.md).
