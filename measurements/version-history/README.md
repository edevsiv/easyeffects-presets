# Version history — FASE 03 engineering pass

Date: 2026-08-02

Evidence type for this pass: **design-audit** (parameter analysis vs stated objectives + DSP handbook). Listening A/B logs still required for MOS validation.

## voice-boost-02

- **Why:** Speech presets must preserve center intelligibility; amount=20 bass + stereo-base=15 + exciter=18 contradict voice clarity engineering (masking + center collapse + sibilance risk). Reduced to moderate enhancer levels aligned with voice-boost-01 philosophy while keeping autogain/multiband leveling.
- **What changed:** `{'bass_amount': 20.0, 'bass_blend': 30.0, 'stereo_base': 15.0, 'exciter_amount': 18.0}` → `{'bass_amount': 6.0, 'bass_blend': 10.0, 'stereo_base': 5.0, 'exciter_amount': 8.0}`
- **Expected result:** Better alignment with category primary metrics; less masking/fatigue; limiter behaviour unchanged in topology.
- **Benchmark:** Re-score datasheet; run A/B vs previous commit per AB_TESTING.md.

## gaming-02

- **Why:** Competitive/immersion balance: Bass Enhancer 20 and stereo-base 15 risk masking 2–6 kHz positional cues (Sonar competitive practice / ITD-ILD stability). Reduced bass/width/exciter while retaining multiband density and presence EQ boosts.
- **What changed:** `{'bass_amount': 20.0, 'stereo_base': 15.0, 'exciter_amount': 18.0}` → `{'bass_amount': 10.0, 'stereo_base': 8.0, 'exciter_amount': 10.0}`
- **Expected result:** Better alignment with category primary metrics; less masking/fatigue; limiter behaviour unchanged in topology.
- **Benchmark:** Re-score datasheet; run A/B vs previous commit per AB_TESTING.md.

## cinema-02

- **Why:** Movie immersion still desired, but stereo-base=15 + bass amount=20 commonly collapses dialog center and muddies 200–500 Hz region. Trimmed toward cinema-01 dialog priorities while keeping heavy leveling stack.
- **What changed:** `{'bass_amount': 20.0, 'stereo_base': 15.0}` → `{'bass_amount': 14.0, 'stereo_base': 10.0}`
- **Expected result:** Better alignment with category primary metrics; less masking/fatigue; limiter behaviour unchanged in topology.
- **Benchmark:** Re-score datasheet; run A/B vs previous commit per AB_TESTING.md.

## music-hd-02

- **Why:** Music Fidelity metric: identical ultra-aggressive enhancer block as experimental fxsound stack over-processes well-mastered music (fatigue + transient smear). Moved toward moderated commercial enhancement closer to music-hd-01 exciters.
- **What changed:** `{'bass_amount': 20.0, 'exciter_amount': 18.0, 'stereo_base': 15.0}` → `{'bass_amount': 12.0, 'exciter_amount': 10.0, 'stereo_base': 8.0}`
- **Expected result:** Better alignment with category primary metrics; less masking/fatigue; limiter behaviour unchanged in topology.
- **Benchmark:** Re-score datasheet; run A/B vs previous commit per AB_TESTING.md.

## fxsound-ultimate-02

- **Why:** Experimental FxSound-inspired preset retains high bass/exciter by design; stereo-base trimmed 15→12 for slightly better mono fold-down without removing Surround analogue character.
- **What changed:** `{'stereo_base': 15.0, 'threshold': -0.8}` → `{'stereo_base': 12.0}`
- **Expected result:** Better alignment with category primary metrics; less masking/fatigue; limiter behaviour unchanged in topology.
- **Benchmark:** Re-score datasheet; run A/B vs previous commit per AB_TESTING.md.

