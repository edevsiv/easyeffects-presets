# Preset version history

Ledger of intent and changes for each shipped preset.  
JSON files today embed EasyEffects parameters; this document is the **human changelog** and design record.

Protocol for edits: [../docs/methodology/TEST_PROTOCOL.md](../docs/methodology/TEST_PROTOCOL.md)

---

## cinema-01

| Field | Content |
|-------|---------|
| **Path** | `presets/movie/cinema-01.json` |
| **Objective** | Balanced cinematic playback with dialog presence and controlled bass |
| **Use case** | Everyday films/series on headphones or PC speakers |
| **Chain** | Equalizer → Bass Enhancer → Compressor → Limiter |
| **v1.0.0** | Initial import from project sources; documented in FASE 01 |
| **Improvements planned** | Night-mode sibling; dialog-focused EQ revision after measurement logs |

## cinema-02

| Field | Content |
|-------|---------|
| **Path** | `presets/movie/cinema-02.json` |
| **Objective** | Dense, leveled “streaming cinema” presentation |
| **Use case** | Action / inconsistent loudness content |
| **Chain** | Autogain → Multiband Compressor → Equalizer → Exciter → Bass Enhancer → Stereo Tools → Limiter |
| **v1.0.0** | Initial heavy cinematic stack |
| **v1.0.1-eng** | FASE 03 design-audit: bass amount 20→14, stereo-base 15→10 for dialog center / mud control ([log](../measurements/version-history/cinema-02-2026-08-02.md)) |
| **Improvements planned** | Human A/B on P0 hardware; optional night-mode DRC sibling |

## music-hd-01

| Field | Content |
|-------|---------|
| **Path** | `presets/music/music-hd-01.json` |
| **Objective** | Clean music clarity with tasteful excitement and width |
| **Use case** | Pop/rock/electronic critical-casual listening |
| **Chain** | Equalizer → Exciter → Stereo Tools → Limiter |
| **v1.0.0** | Initial HD music path |
| **Improvements planned** | AutoEQ variant hooks |

## music-hd-02

| Field | Content |
|-------|---------|
| **Path** | `presets/music/music-hd-02.json` |
| **Objective** | Louder, more commercial music enhancement |
| **Use case** | Playlists, background listening, weak speakers |
| **Chain** | Autogain → Multiband → Equalizer → Exciter → Bass → Stereo → Limiter |
| **v1.0.0** | Initial enhanced music stack |
| **v1.0.1-eng** | FASE 03: moderated bass/exciter/width for Music Fidelity ([log](../measurements/version-history/music-hd-02-2026-08-02.md)) |
| **Improvements planned** | Compare vs FxSound Music presets in measurements |

## classic-music-01

| Field | Content |
|-------|---------|
| **Path** | `presets/music/classic-music-01.json` |
| **Objective** | Preserve dynamics; gentle tone + space |
| **Use case** | Classical, jazz, acoustic |
| **Chain** | Equalizer → Reverb → Limiter |
| **v1.0.0** | Initial classical path |
| **Improvements planned** | Even drier default; reverb as optional wet only |

## gaming-01

| Field | Content |
|-------|---------|
| **Path** | `presets/gaming/gaming-01.json` |
| **Objective** | Competitive clarity and controlled punch |
| **Use case** | FPS / awareness-focused play |
| **Chain** | Equalizer → Bass Enhancer → Stereo Tools → Compressor → Limiter |
| **v1.0.0** | Initial competitive gaming path |
| **Improvements planned** | Footstep-oriented EQ pass inspired by Sonar competitive culture |

## gaming-02

| Field | Content |
|-------|---------|
| **Path** | `presets/gaming/gaming-02.json` |
| **Objective** | Immersive single-player presentation |
| **Use case** | RPG / cinematic games |
| **Chain** | Autogain → Multiband → Equalizer → Exciter → Bass → Stereo → Limiter |
| **v1.0.0** | Initial immersive gaming stack |
| **v1.0.1-eng** | FASE 03: reduced bass/width/exciter to protect 2–6 kHz cues ([log](../measurements/version-history/gaming-02-2026-08-02.md)) |
| **Improvements planned** | Latency notes vs quantum; human A/B vs gaming-01 |

## voice-boost-01

| Field | Content |
|-------|---------|
| **Path** | `presets/voice/voice-boost-01.json` |
| **Objective** | Speech intelligibility for podcasts and talks |
| **Use case** | YouTube essays, courses, dialogue rescue |
| **Chain** | Equalizer → Gate → Compressor → De-esser → Limiter |
| **v1.0.0** | Initial speech path |
| **Improvements planned** | Long-form fatigue test; gate tuning |

## voice-boost-02

| Field | Content |
|-------|---------|
| **Path** | `presets/voice/voice-boost-02.json` |
| **Objective** | Stronger leveling for mixed speech + music beds |
| **Use case** | Variety content when `voice-boost-01` is too mild |
| **Chain** | Autogain → Multiband → Equalizer → Exciter → Bass → Stereo → Limiter |
| **v1.0.0** | Initial enhanced voice/content stack |
| **v1.0.1-eng** | FASE 03: cut extreme bass/width/exciter conflicting with Voice Clarity ([log](../measurements/version-history/voice-boost-02-2026-08-02.md)) |
| **Improvements planned** | Human A/B vs voice-boost-01; naming clarity |

## volume-booster-01

| Field | Content |
|-------|---------|
| **Path** | `presets/experimental/volume-booster-01.json` |
| **Objective** | Raise perceived loudness safely |
| **Use case** | Quiet devices; low system volume |
| **Chain** | Equalizer → Compressor → Limiter |
| **v1.0.0** | Initial loudness helper |
| **Improvements planned** | Explicit LUFS-oriented autogain sibling |

## fxsound-ultimate-02

| Field | Content |
|-------|---------|
| **Path** | `presets/experimental/fxsound-ultimate-02.json` |
| **Objective** | FxSound-inspired wide/exciting enhancer chain |
| **Use case** | Windows FxSound migrants; wow-factor listening |
| **Chain** | Autogain → Multiband → Equalizer → Exciter → Bass → Stereo → Limiter |
| **v1.0.0** | Initial experimental enhancer |
| **v1.0.1-eng** | FASE 03: stereo-base 15→12 for mono fold-down; mapping doc added ([log](../measurements/version-history/fxsound-ultimate-02-2026-08-02.md)) |
| **Improvements planned** | Split clarity/bass variants after A/B vs real FxSound |

---

## How to bump history

When changing a JSON preset:

1. Run the test protocol + A/B protocol
2. Add a new dated section under the preset (`v1.1.0`, `v1.1.1`, …)
3. Add `measurements/version-history/<preset>-YYYY-MM-DD.md`
4. Update datasheet scores
5. Update [../CHANGELOG.md](../CHANGELOG.md)
