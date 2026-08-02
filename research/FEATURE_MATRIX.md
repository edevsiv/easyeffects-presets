# Feature matrix — commercial suites vs EasyEffects

Legend: **Yes** = first-class in EasyEffects · **Partial** = approximate with plugins/chains · **No** = not available / requires external tools · **N/A** = not a design goal of that product

| Technology | Voice Enhancement | Bass Enhancement | Stereo Expansion | Dynamic Compression | Limiter | Equalizer | Virtualization | Automatic Gain | Loudness | Exciter |
|------------|:-----------------:|:----------------:|:----------------:|:-------------------:|:-------:|:---------:|:--------------:|:--------------:|:--------:|:-------:|
| **EasyEffects** | Partial (EQ + Gate + De-esser + Speech) | Yes (`bass_enhancer`, `bass_loudness`) | Yes (`stereo_tools`) | Yes (comp / multiband) | Yes | Yes (up to 32 bands) | Partial (Crossfeed, Crosstalk Canceller, Convolver/HRTF) | Yes (`autogain`) | Yes (`loudness`) | Yes (`exciter` / Crystalizer) |
| **FxSound** | Partial (EQ + Clarity) | Yes (Bass effect) | Yes (Surround / Ambience) | Yes (Dynamic Boost) | Partial (peak control in Dynamic Boost) | Yes (multi-band) | Partial (Surround) | Partial (Dynamic Boost) | Partial | Partial (Fidelity) |
| **Dolby Audio (PC)** | Yes (dialog / Intelligent EQ family) | Partial (EQ / speaker opt) | Yes (Surround Decoder + Virtualizer) | Yes (DRC / Regulator) | Yes (Volume Maximizer look-ahead) | Yes | Yes (HRTF Virtualizer) | Yes (Volume Leveler) | Yes (Dolby Volume) | No / proprietary |
| **DTS:X / Sound Unbound** | Partial (dialog clarity modes) | Yes (OEM modes) | Yes (spatial) | Partial | Partial | Yes | Yes (Headphone:X / Ultra) | Partial | Partial | No |
| **SteelSeries Sonar** | Yes (chat channel EQ + mic FX) | Yes (EQ) | Yes (spatial modes) | Partial (Smart Volume) | Partial | Yes (parametric) | Yes (360° spatial) | Partial | Partial | No |
| **Peace + Equalizer APO** | Via configs | Via EQ / VST | Via VST / matrix | Via VST | Via VST | Yes (APO core) | Via HeSuVi / VST | Via VST | Via VST | Via VST |
| **Waves MaxxAudio** | Yes (MaxxVoice / dialog) | Yes (MaxxBass) | Yes (MaxxStereo / Space) | Yes | Yes | Yes | Partial | Yes | Yes | Partial |
| **Nahimic** | Partial | Yes | Yes | Partial | Partial | Yes | Yes (spatial) | Partial | Partial | No |
| **Realtek Audio Console** | Partial | Yes | Partial (surround) | Partial | Partial | Yes | Partial | Partial | Partial | No |

## EasyEffects reproduction notes

| Commercial feature | Closest EasyEffects approach |
|--------------------|------------------------------|
| FxSound Fidelity / Clarity | Exciter + Crystalizer + gentle high-shelf EQ |
| FxSound Ambience | Reverb (very light) or Convolver room IR |
| FxSound Surround | Stereo Tools width / side gain; optional Crosstalk Canceller |
| FxSound Dynamic Boost | Autogain + Compressor or Multiband Compressor + Limiter |
| FxSound Bass | Bass Enhancer (+ optional Bass Loudness) |
| Dolby Voice / Dialog | EQ presence (2–4 kHz) + Gate + De-esser; Speech processor on input |
| Dolby Volume Leveler | Autogain (EBU R128 targets) |
| Dolby Volume Maximizer | Maximizer / Limiter with careful ceiling |
| Dolby Virtual Surround | Convolver with HRTF/SOFA or Crosstalk Canceller (speakers) — **gap vs OEM HRTF DB** |
| DTS Headphone:X | Convolver HRTF packs + Stereo Tools; Windows spatial APIs **not** available |
| Sonar per-app EQ | EasyEffects per-app effects / PipeWire routing (less polished UI) |
| Peace system-wide EQ | EasyEffects Equalizer (app-scoped by default) |
| MaxxBass | Bass Enhancer harmonics |
| Nahimic spatial | Same virtualization gap as Dolby/DTS |

## Gaps (cannot fully reproduce in EasyEffects alone)

1. Proprietary **OEM speaker tuning** curves baked into laptop firmware/drivers.
2. Licensed **HRTF databases** with 500+ headphone profiles (DTS).
3. Windows **Spatial Sound** object renderers (DTS:X / Dolby Atmos for Headphones).
4. Closed **AI noise** models identical to ClearCast / OEM suites (RNNoise / DeepFilterNet are alternatives on **input**).
5. Bit-identical clones of FxSound `DfxDsp` internals (even though FxSound is open source, ports are non-trivial).

## Decision rule for this project

If a feature is **Yes** or **Partial**, it may enter a preset after protocol testing.  
If it is a **gap**, document it in research notes and prefer honest approximation over fake marketing claims.
