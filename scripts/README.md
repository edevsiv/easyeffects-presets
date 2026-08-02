# Scripts

| Script | Purpose |
|--------|---------|
| [install.sh](install.sh) | Copy presets into the EasyEffects output directory |
| [validate.sh](validate.sh) | Validate JSON presets and repository structure |
| [check_markdown_links.py](check_markdown_links.py) | Check relative Markdown links |

```bash
chmod +x scripts/*.sh
./scripts/validate.sh
./scripts/install.sh --dry-run
```
