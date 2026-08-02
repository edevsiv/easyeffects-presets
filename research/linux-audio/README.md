# Research: Linux audio ecosystem

## Stack layers

```text
Apps → PipeWire → EasyEffects (filter) → Device drivers → Hardware
         ↘ WirePlumber (session)
```

## Relevant open projects

| Project | Relevance |
|---------|-----------|
| EasyEffects | Our host |
| LSP / Calf / Zam | Plugin backends |
| AutoEQ | Headphone correction targets |
| HeSuVi-related open IRs | Virtual surround experiments |
| Community EasyEffects preset repos | Benchmark peers |

## Philosophy

Commercial suites optimize for **one-click wow** on OEM hardware.  
This project optimizes for **reproducible, documented, open chains** that users can audit and fork.
