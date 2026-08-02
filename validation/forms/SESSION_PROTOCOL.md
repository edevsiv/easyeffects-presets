# Official listening-test protocol

Companion to [LISTENING_FORM.md](LISTENING_FORM.md) and [../../docs/methodology/AB_TESTING.md](../../docs/methodology/AB_TESTING.md).

## Before the session

1. Register or select **Hardware ID** and **Listener ID**.
2. Fix PipeWire clock (prefer 48 kHz, quantum noted).
3. Disable competing OEM DSP (Dolby/Nahimic/FxSound) when comparing.
4. Install preset revision under test (`./scripts/install.sh`).
5. Prepare content from [../../references/](../../references/).

## Session flow

1. **Warm-up** 2–3 min Flat (bypass).
2. Level-match Flat vs preset (perceived loudness, not only peaks).
3. Listen **≥ 20 s** excerpts; for fatigue, continue to **≥ 15 min** when claiming V5.
4. Score questionnaire metrics independently before discussing.
5. Optional second pass with alternate anchor (FxSound/Dolby notes).
6. File form under the campaign `sessions/` folder.
7. Update profile dossier + STATUS only if CERTIFICATION gates pass.

## Required fields (non-negotiable)

Hardware · Distro · PipeWire · EasyEffects · Content · Preset · Volume · Comparison · Duration · Observations · Scores
