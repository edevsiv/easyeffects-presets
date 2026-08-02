# Website architecture (planned)

```text
Git repo (Markdown + JSON indexes)
        ↓
Static site generator
        ↓
Pages: Home · Downloads · Profiles · Hardware · FAQ · Benchmark · Research · Roadmap · Search
        ↓
Search index built from platform/database/profiles.json + hardware scorecards
```

## Principles

- Docs-as-code (PRs update site)
- No proprietary media
- Seals rendered from `validation/STATUS.md` / profiles.json — never hand-waved on the homepage
