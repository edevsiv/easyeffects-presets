# Official IR selection (FASE 05)

## Selected candidate: IRCAM LISTEN (download-yourself)

| Criterion | Assessment |
|-----------|------------|
| License | Free for research/personal use per IRCAM Listen terms — **do not vendor binaries** until redistribution rights confirmed for MIT repo |
| Quality | Established multi-subject HRIR database; widely cited |
| Compatibility | WAV available; resample to PipeWire rate (often 48 kHz) for EasyEffects Convolver |
| Latency | Convolution length dependent; unsuitable for lowest-latency competitive gaming until measured |
| Origin | http://recherche.ircam.fr/equipes/salles/listen/ |

## Why this IR

Best balance of documentation, research pedigree, and open access among catalog candidates ([SELECTION.md](SELECTION.md)).

## Integration status

| Step | Status |
|------|--------|
| Selected | **Yes** |
| Vendored in repo | **No** (license-safe stance) |
| Convolver preset | **Not yet** |
| User instructions | Download subject archive → convert/resample → EasyEffects Convolver import |

## Secondary candidate

MIT KEMAR — keep as alternate after license re-check.
