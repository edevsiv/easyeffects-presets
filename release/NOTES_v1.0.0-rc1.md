# Release notes — v1.0.0-rc1

**Title:** EasyEffects Presets Premium — Validation Campaign RC

## Highlights

- Full open-source repository with research lab, metrics, and datasheets
- First official validation campaign **VC-2026-08** on Acer Nitro + EasyEffects 8.2.8
- Real EasyEffects UI screenshots for all 11 presets
- EE8 compatibility migrations for legacy bass enhancer / limiter fields
- Install script updated for Flatpak XDG data preset path

## Preset seals

Mostly **Beta**; `fxsound-ultimate-02` remains **Experimental**.

## Not in this RC

- Full subjective A/B vs FxSound/Dolby across all content classes
- **Validated** / **Stable** seals
- Vendored Convolver IR binaries
- Automatic AutoEQ → full preset writer

## Install

```bash
git clone https://github.com/edevsiv/easyeffects-presets.git
cd easyeffects-presets
./scripts/install.sh --flatpak   # or --native
```

## Verify

```bash
./scripts/validate.sh
```
