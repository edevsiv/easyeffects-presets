# PipeWire guide for EasyEffects presets

EasyEffects processes audio **inside the PipeWire graph**. Buffer size, quantum, and sample rate affect latency, CPU use, and how stable heavy presets feel.

## Concepts

| Term | Meaning |
|------|---------|
| **Sample rate** | Samples per second (e.g. 48000 Hz). Higher rates need more CPU. |
| **Quantum / buffer** | Frames processed per cycle. Smaller = lower latency, higher CPU and xruns risk. |
| **Latency** | Delay from app output to speakers/headphones. |
| **Xrun** | Underrun/overrun — audible glitches when the graph cannot keep up. |

## Recommended starting point

For desktop listening (music, movies, casual gaming):

- Sample rate: **48000 Hz**
- Quantum: **1024** (or distro default)
- WirePlumber session manager running

For competitive gaming / monitoring:

- Try quantum **256** or **512** if CPU allows
- Prefer lighter presets (`gaming-01`) before heavy chains (`*-02`)

## Checking current status

```bash
pw-top
# or
pactl info | grep -E 'Server Name|Sample Specification'
```

PipeWire replaces PulseAudio for most apps via `pipewire-pulse`.

## Compatibility with EasyEffects

1. Start PipeWire + WirePlumber before EasyEffects.
2. Enable EasyEffects **service** / autostart if you want filters always on.
3. Exclude EasyEffects itself from being processed (handled by the app blocklist).
4. Avoid stacking another system-wide EQ (PulseEffects remants, separate LADSPA sinks) unless you know the routing.

## Flatpak notes

Flatpak EasyEffects talks to the host PipeWire socket. Permissions are usually correct from Flathub; if apps do not appear:

```bash
flatpak permission-set pipewire easyeffects yes  # only if your setup requires it
```

Prefer fixing PipeWire/session issues on the host rather than forcing odd sample rates inside the sandbox.

## Tuning tips for this preset pack

| Preset style | PipeWire tip |
|--------------|--------------|
| Cinema / multiband / stereo tools | Keep quantum ≥ 512–1024 to avoid xruns |
| Voice boost | Moderate settings; gate/compressor are light |
| Volume booster / FxSound-like | Watch clipping; limiter is mandatory |
| Music HD | Stable 48 kHz is enough for most gear |

## Sample WirePlumber / PipeWire overrides (advanced)

Create user overrides only if you understand the impact. Example quantum hint (paths vary by distro):

```text
~/.config/pipewire/pipewire.conf.d/99-quantum.conf
```

```conf
context.properties = {
  default.clock.rate          = 48000
  default.clock.allowed-rates = [ 44100 48000 96000 ]
  default.clock.quantum       = 1024
  default.clock.min-quantum   = 32
  default.clock.max-quantum   = 2048
}
```

Restart PipeWire after changes:

```bash
systemctl --user restart pipewire pipewire-pulse wireplumber
```

Example fragments also live in [`../pipewire/`](../pipewire/).

## Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Crackling | Quantum too small / CPU spike | Raise quantum; close heavy apps |
| High delay in games | Large buffer + heavy FX | Lower quantum; use lighter preset |
| No effect | App not in EasyEffects / wrong device | Select correct output; enable process all inputs |
| Flatpak missing apps | Permissions / portal | Update Flatpak; check host PipeWire |

See also: [INSTALL.md](INSTALL.md) and the [PipeWire wiki](https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/home).
