# Open IR / HRTF catalog

**No binary IRs are vendored yet.** This catalog lists candidate open sources for future Convolver presets.

| Dataset | Type | License / access | Use case | Notes |
|---------|------|------------------|----------|-------|
| [MIT KEMAR](https://sound.media.mit.edu/resources/KEMAR.html) | HRTF | Historically widely used in research; verify current terms | Headphone virtualization experiments | Classic dummy-head |
| [IRCAM LISTEN](http://recherche.ircam.fr/equipes/salles/listen/) | HRIR | Free for research/personal (check site) | Binaural / subject HRTFs | WAV/MAT; also SOFA mirrors |
| [SOFA repository](https://sofaconventions.org/mediawiki/index.php/Files) | HRTF/BRIR/DRIR | Per-dataset | Interchange format | Needs conversion to WAV/IRS for EE |
| [ARI HRTF](https://www.oeaw.ac.at/isf/das-institut/software/hrtf-database) | HRTF | Check institute terms | Research virtualization | ITE/BTE sets |
| [SADIE](https://www.york.ac.uk/sadie-project/) | HRTF | Project license | Multi-subject | Academic |
| OpenAL Soft utils (KEMAR/LISTEN defs) | Build scripts | OpenAL Soft license | Pipeline reference | Not drop-in EE IRs |
| AutoEQ convolution WAVs | FIR correction | Per AutoEq output | Headphone correction via Convolver | Alternative to parametric EQ |
| Community HeSuVi-compatible open matrices | Surround matrix | **Verify each file** | Virtual surround | Avoid unknown redistrib |

## EasyEffects Convolver requirements

- Prefer WAV / IRS compatible with zita-convolver backend
- Match sample rate to PipeWire graph (often 48 kHz) or allow EE resample
- Apply input gain / autogain carefully — IRs can add energy
- Document latency impact for gaming presets

## Acceptance checklist before adding an IR to the repo

1. License allows redistribution in this MIT project **or** document “download yourself” only
2. Source URL + hash recorded
3. Mono/stereo layout explained
4. Listening smoke test + datasheet note
5. No copyrighted movie/music impulse captures

See [../../docs/audio-engine/Convolver.md](../../docs/audio-engine/Convolver.md).
