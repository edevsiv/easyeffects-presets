# AutoEQ workspace

| Item | Purpose |
|------|---------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | Integration design |
| [INTEGRATION.md](INTEGRATION.md) | Future integration milestones |
| [WORKFLOW.md](WORKFLOW.md) | End-user workflow |
| [convert_apo_to_bands.py](convert_apo_to_bands.py) | Experimental APO → band table (no EE JSON write) |
| [recommend.py](recommend.py) | Markdown recommendations (no preset mutation) |
| [recommendations/](recommendations/) | Generated reports |
| [examples/ParametricEQ.sample.txt](examples/ParametricEQ.sample.txt) | Sample APO file |

```bash
python3 autoeq/convert_apo_to_bands.py autoeq/examples/ParametricEQ.sample.txt --markdown
python3 autoeq/recommend.py autoeq/examples/ParametricEQ.sample.txt \
  --headphone "Example-IEM" --content-preset music-hd-01 \
  -o autoeq/recommendations/example-iem.md
```

Production path remains: EasyEffects Equalizer **APO** import.  
Platform search hook: [platform/tools/SEARCH_DESIGN.md](../platform/tools/SEARCH_DESIGN.md).
