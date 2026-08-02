# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 1.x     | Yes       |
| < 1.0   | No        |

## Reporting a vulnerability

This repository primarily ships **JSON audio presets** and documentation. Risk is low, but we still take reports seriously (malicious PRs, CI secrets, supply-chain issues in scripts).

Please report security concerns privately:

1. Prefer [GitHub Security Advisories](https://github.com/edevsiv/easyeffects-presets/security/advisories/new) if available.
2. Or email the maintainer listed in the repository profile / README credits.

Include:

- Description of the issue
- Steps to reproduce
- Potential impact
- Suggested fix (optional)

We aim to acknowledge reports within **7 days** and publish a fix or mitigation as soon as practical.

## Scope

**In scope**

- Install / validation scripts that could execute unexpected commands
- CI workflow secrets or unsafe actions
- Links or downloads that could lead to malware

**Out of scope**

- Subjective audio quality of presets
- Upstream EasyEffects / PipeWire / plugin bugs (report those upstream)

## Best practices for users

- Prefer cloning from the official repository: `https://github.com/edevsiv/easyeffects-presets`
- Review `scripts/*.sh` before running them with elevated privileges
- Never run untrusted JSON through custom converters without inspection
