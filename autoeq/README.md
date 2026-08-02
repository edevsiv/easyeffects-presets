# AutoEQ workspace

| Item | Purpose |
|------|---------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | Integration design |
| [convert_apo_to_bands.py](convert_apo_to_bands.py) | Experimental APO → band table (no EE JSON write) |
| [examples/ParametricEQ.sample.txt](examples/ParametricEQ.sample.txt) | Sample APO file |

```bash
python3 autoeq/convert_apo_to_bands.py autoeq/examples/ParametricEQ.sample.txt --markdown
```

Production path remains: EasyEffects Equalizer **APO** import.
