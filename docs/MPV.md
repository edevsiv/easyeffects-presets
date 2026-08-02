# MPV + EasyEffects for movies

Use **mpv** for decoding/playback and **EasyEffects** for system-wide (or app-routed) processing. This avoids fighting two EQs inside the same path when configured deliberately.

## Goals

- Clear dialogue on stereo headphones/speakers
- Sensible downmix of **5.1 / 7.1** cinema tracks
- Stable loudness when combined with `presets/movie/cinema-*.json`

## Example `mpv.conf`

A starter file is shipped at [`../mpv/mpv.conf`](../mpv/mpv.conf). Copy or merge into:

```text
~/.config/mpv/mpv.conf
```

Highlights:

- Prefer PipeWire / Pulse output (`ao=pipewire` or `ao=pulse`)
- Optional volume normalization (`loudnorm` or ReplayGain) — **disable** if EasyEffects Autogain already handles level
- Explicit stereo downmix for multi-channel sources

## Downmix (5.1 → stereo)

Films often ship discrete surround. On stereo headphones you want a controlled fold-down:

```conf
# Force stereo output from mpv
audio-channels=stereo

# Or let the mixer handle it (PipeWire/EasyEffects)
# audio-channels=auto
```

Tips:

1. Prefer **one** place for heavy bass management — either mpv filters **or** EasyEffects Bass Enhancer, not both at maximum.
2. For night listening, EasyEffects cinema presets with compressor/limiter help more than crushing dynamic range inside mpv alone.
3. Keep mpv volume near 100% and trim in EasyEffects if you use Autogain / Limiter chains (`cinema-02`).

## Suggested pairing

| Content | mpv | EasyEffects preset |
|---------|-----|--------------------|
| Modern action / streaming | stereo downmix | `cinema-02` |
| Dialogue-heavy drama | stereo | `cinema-01` or `voice-boost-01` |
| Concert / music film | stereo, minimal mpv FX | `music-hd-01` / `classic-music-01` |

## Filmes 5.1 — checklist

1. Confirm the file really has 5.1 (`mpv` OSD / `ffprobe`).
2. Set `audio-channels=stereo` **or** configure PipeWire to downmix consistently.
3. Load a **movie** preset in EasyEffects.
4. Disable competing enhancements (TV “night mode”, browser Loudness, double Autogain).
5. If dialogue is still buried, try `voice-boost-01` temporarily, then retune EQ.

## Conflicts to avoid

- mpv `af=lavcac3` / exotic resamplers + EasyEffects Exclusive mode oddities
- Running PulseEffects **and** EasyEffects together
- HDMI passthrough of raw bitstream (AC3/DTS) — EasyEffects cannot process encoded passthrough; decode to PCM first

## Related

- [INSTALL.md](INSTALL.md)
- [PIPEWIRE.md](PIPEWIRE.md)
- [../presets/movie/README.md](../presets/movie/README.md)
