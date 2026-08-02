# Release strategy

## Channels

| Channel | Meaning | Git |
|---------|---------|-----|
| **Nightly** | Docs/platform snapshots; may be main HEAD | optional `nightly/*` notes |
| **Experimental** | Profiles/features with known risk | seal + prerelease tag optional |
| **Beta** | UI-compatible shipping profiles | `vX.Y.Z-rcN` or beta seals |
| **Validated** | Listening gates passed (per profile) | seal in STATUS — not necessarily a tag |
| **Stable** | Product release meeting checklist | `vX.Y.Z` |
| **Reference** | Multi-listener / multi-HW gold | seal + docs designation |

## Rules

1. Profile seals and git tags are related but not identical (a Stable tag may still contain Experimental profiles).
2. `v1.0.0` Stable is **released** (VC-2026-08-LISTEN). Further Stable tags still require checklist sign-off.
3. Data releases (IR packs) SHOULD use separate archives with license files.
4. Nightly never implies certification.
