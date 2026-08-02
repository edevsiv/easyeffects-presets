# Project governance

## Roles

| Role | Responsibility |
|------|----------------|
| Maintainer | Seals, releases, architecture decisions |
| Reviewer | PR technical review |
| Listener | Subjective sessions under protocol |
| Hardware reporter | Device scorecards + evidence |

## Review flow

```text
Issue / proposal → PR → CI (validate.sh) → reviewer → maintainer merge
                              ↓
                    DSP changes need methodology note
                    Seal changes need CERTIFICATION evidence
```

## Acceptance criteria

| Change type | Required |
|-------------|----------|
| Docs / platform | Clear links, no contradictory seals |
| Preset JSON | Datasheet + HISTORY + validate.sh + rationale |
| Seal promotion | CERTIFICATION gates + linked forms |
| Hardware scorecard | Device sheet + evidence path |
| IR / AutoEQ data | License statement |

## Certification policy

Seals are **evidence-bound**. Maintainers MUST NOT promote Validated/Stable/Reference
without meeting [validation/CERTIFICATION.md](../validation/CERTIFICATION.md).

## Release policy

See [RELEASE_STRATEGY.md](RELEASE_STRATEGY.md). Stable tags require checklist sign-off.
