# Selected open IR candidates — checklist

No binaries vendored yet. Candidates for future Convolver presets:

| Candidate | Origin | License check | Quality notes | EE compatibility | Decision |
|-----------|--------|---------------|---------------|------------------|----------|
| MIT KEMAR HRTF | MIT Media Lab historic set | Verify current redistribution terms before vendor | Classic research HRTF | Convert to WAV/IRS @ graph rate | **Candidate** |
| IRCAM LISTEN | IRCAM Listen DB | Free research/personal — confirm before repo vendor | Multi-subject HRIR | WAV available; resample 44.1→48k | **Candidate** |
| SOFA mirrors (TU-Berlin KEMAR etc.) | sofaconventions.org | Per-file | Good interchange | Needs SOFA→WAV tooling | **Candidate** |
| AutoEQ FIR WAV | AutoEQ output | User-generated | Headphone correction | Convolver import | **Workflow** (user-local) |
| Random HeSuVi packs | Community | Often unclear | Mixed | Risky | **Reject until license clear** |

## Acceptance checklist (must pass)

- [ ] License allows MIT repo redistribution **or** documented download-yourself only
- [ ] Source URL + version/date recorded
- [ ] Channel layout documented (L/R)
- [ ] Sample rate strategy defined
- [ ] Smoke test in EasyEffects Convolver
- [ ] Latency noted for gaming presets

See [catalog/README.md](catalog/README.md).
