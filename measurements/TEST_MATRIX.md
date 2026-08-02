# Test matrix — all presets

Each row is a required technical fiche. Details live in [datasheets/](datasheets/).

| Preset | Objective | Hardware focus | Key plugins | EQ intent | Comp / MB | Limiter | Stereo | Bass | Expected | Limitations |
|--------|-----------|----------------|-------------|-----------|-----------|---------|--------|------|----------|-------------|
| cinema-01 | Balanced cinema | HP / notebook | EQ Comp Bass Lim | Dialog + mild LFE | Broadband mild | −1 dB | — | amt 6 | Clear dialog | No autogain |
| cinema-02 | Immersive leveled | HP / notebook | AG MB EQ Exc Bass ST Lim | Bass shelf + presence | Multiband | −0.8 | base 10 | amt 14 | Dense cinema | Fatigue if stacked OEM |
| music-hd-01 | Clean music HD | DAC + HP | EQ Exc ST Lim | Smile-ish, cut mud | — | −1 | base 0.15 | — | Air + width | No AutoEQ |
| music-hd-02 | Enhanced music | Notebook / casual | AG MB EQ Exc Bass ST Lim | Low boost + air | Multiband | −0.8 | base 8 | amt 12 | Loud playlists | Not fidelity-first |
| classic-music-01 | Dynamic classical | Neutral HP | EQ Reverb Lim | Gentle HF | — | −1.5 | — | — | Space, intact DR | Reverb taste |
| gaming-01 | Competitive | Headset | EQ Bass ST Comp Lim | 2–8 kHz cues | Mild | −1 | base 0.25 | amt 5 | Footsteps | Bright fatigue |
| gaming-02 | Immersion | Headset | AG MB EQ Exc Bass ST Lim | Presence cluster | Multiband | −0.8 | base 8 | amt 10 | Exciting worlds | < positional purity |
| voice-boost-01 | Speech | Any HP | EQ Gate Comp Deess Lim | Mid forward, cut rumble | Voice ratio | −1 | — | — | Intelligibility | Output-only |
| voice-boost-02 | Leveled speech+beds | Notebook | AG MB EQ Exc Bass ST Lim | 1.6–4 kHz lift | Multiband | −0.8 | base 5 | amt 6 | Consistent speech | Hybrid chain |
| volume-booster-01 | Loudness | Quiet devices | EQ Comp Lim | Flat +2 dB | Makeup 6 | −0.5 / in+6 | — | — | Louder | Crude shelf |
| fxsound-ultimate-02 | FxSound-like | Notebook speakers | AG MB EQ Exc Bass ST Lim | Strong lows + mid | Multiband | −0.8 | base 12 | amt 20 | Wow factor | Fatigue / not HR |

## Calibration method (scientific workflow)

```text
1. Declare objective + primary metrics
2. Extract / set plugin parameters (datasheet)
3. design-audit scorecard
4. A/B vs previous + Flat (+ FxSound/Dolby when relevant)
5. Log subjective + any objective meters
6. Accept / reject / iterate → version-history entry
```

See [../docs/methodology/TEST_PROTOCOL.md](../docs/methodology/TEST_PROTOCOL.md) and [../docs/methodology/AB_TESTING.md](../docs/methodology/AB_TESTING.md).
