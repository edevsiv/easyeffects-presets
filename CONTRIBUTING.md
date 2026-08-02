# Contributing

Thanks for helping improve **EasyEffects Presets Premium**. Contributions of presets, docs, scripts, and fixes are welcome.

## Code of conduct

Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

- New or improved EasyEffects **output** presets (JSON)
- Documentation fixes and translations
- Installer / validation script improvements
- Screenshots and A/B listening notes
- Bug reports and feature requests via GitHub Issues

## Development setup

1. Fork and clone the repository:

   ```bash
   git clone https://github.com/<your-user>/easyeffects-presets.git
   cd easyeffects-presets
   ```

2. Install EasyEffects and required LV2 plugins (see [docs/INSTALL.md](docs/INSTALL.md)).

3. Validate locally before opening a PR:

   ```bash
   ./scripts/validate.sh
   ```

## Preset guidelines

1. **Category** — place files under the correct folder:

   | Category | Path | Typical use |
   |----------|------|-------------|
   | Movie | `presets/movie/` | Films, series, dialogue clarity |
   | Music | `presets/music/` | Stereo music listening |
   | Gaming | `presets/gaming/` | Footsteps, spatial cues, immersion |
   | Voice | `presets/voice/` | Podcasts, calls, speech |
   | Experimental | `presets/experimental/` | Loudness boosts, FX-inspired chains |

2. **Naming** — use lowercase kebab-case:

   ```text
   <name>-<revision>.json
   ```

   Example: `cinema-03.json`

3. **Format** — valid EasyEffects JSON with an `output` section and `plugins_order`.

4. **Documentation** — update:

   - [presets/README.md](presets/README.md)
   - [presets/HISTORY.md](presets/HISTORY.md)
   - Category `README.md` if present
   - [CHANGELOG.md](CHANGELOG.md) under `### Added` / `### Changed`

5. **Listening protocol** — follow [docs/methodology/TEST_PROTOCOL.md](docs/methodology/TEST_PROTOCOL.md) and [docs/methodology/AB_TESTING.md](docs/methodology/AB_TESTING.md); attach datasheet + version-history for DSP changes.

6. **Safety** — include a limiter (or maximizer used carefully) to avoid clipping when boosting gain.

7. **Do not commit** personal machine paths, IRS binaries larger than needed, or secrets.

## Pull request process

1. Create a focused branch (`feat/music-jazz-01`, `docs/fix-install`, …).
2. Keep commits [conventional](https://www.conventionalcommits.org/) when possible:

   - `feat:` new preset or capability
   - `fix:` correction
   - `docs:` documentation only
   - `chore:` tooling / CI / structure

3. Open a PR using the template and describe listening tests (headphones / speakers / device).
4. Ensure CI passes (`validate-json` workflow).

## Review criteria

- JSON validates
- Naming and folder placement are consistent
- Docs updated
- No destructive script changes without discussion

## Questions

Open a discussion or issue on GitHub. For EasyEffects itself, see [wwmm/easyeffects](https://github.com/wwmm/easyeffects).
