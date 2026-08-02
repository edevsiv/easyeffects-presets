# Official metrics

All preset evaluations use these metrics on a **1.0–5.0** scale (half-steps allowed).  
Scores must cite **evidence type**: `design-audit` | `subjective-log` | `objective-measure` | `ab-test`.

## Scale (shared)

| Score | Meaning |
|------:|---------|
| 1.0 | Fails goal / harmful |
| 2.0 | Weak / inconsistent |
| 3.0 | Acceptable baseline |
| 4.0 | Strong for the category |
| 5.0 | Excellent / reference-grade |

**Rule:** A change that raises one metric by ≥0.5 but drops two others by ≥0.5 without documented trade-off is rejected.

## Metric definitions

### Voice Clarity
Intelligibility of speech (dialog, podcasts, callouts). Anchors: 0.5–4 kHz presence, de-essing, center image stability.

### Bass Control
Low-end impact without mud, boom, or masking of midrange. Anchors: ≤120 Hz behaviour, Bass Enhancer amount, limiter engagement.

### Treble Detail
Air and articulation without sibilance or encode grit. Anchors: ≥6 kHz, Exciter amount, de-esser interaction.

### Stereo Width
Perceived stage width with stable phantom center. Anchors: Stereo Tools `stereo-base` / side level; mono fold-down check.

### Dynamic Control
Consistency of levels without pumping or crushing intent. Anchors: compressor/multiband/autogain behaviour.

### Listening Fatigue
Comfort after **15–20 minutes**. Anchors: harsh highs, constant loudness, enhancer density.

### Perceived Loudness
Subjective loudness vs flat bypass at matched peak risk. Anchors: Autogain target, makeup, limiter ceiling.

### Gaming Positioning
Ability to localize footsteps/utility (L/R and depth cues). Anchors: 2–6 kHz EQ, width not destroying ITD/ILD.

### Movie Immersion
Sense of cinematic weight and surround-like space without dialog loss. Anchors: bass + width + dialog band.

### Music Fidelity
Tonal naturalness and transient integrity for music. Anchors: avoid over-multiband; respect genre dynamics.

## Category weighting (default)

| Category | Primary metrics (weight ×1.5) | Secondary |
|----------|-------------------------------|-----------|
| movie | Voice Clarity, Movie Immersion, Dynamic Control | Bass, Fatigue |
| music | Music Fidelity, Treble Detail, Bass Control | Width, Loudness |
| gaming | Gaming Positioning, Dynamic Control | Bass, Width, Fatigue |
| voice | Voice Clarity, Listening Fatigue | Dynamic, Loudness |
| experimental | Perceived Loudness, Bass Control | Width, Fatigue |

## Minimum evidence for merge

DSP PRs that change JSON require:

1. Updated datasheet scores (at least `design-audit`)
2. Entry in `measurements/version-history/`
3. A/B notes vs previous commit (protocol)
4. No unexplained metric regressions on primary weights
