#!/usr/bin/env bash
# Validate EasyEffects preset JSON files and repository structure.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

REQUIRED_DIRS=(
  presets/movie
  presets/music
  presets/gaming
  presets/voice
  presets/experimental
  docs
  docs/audio-engine
  docs/methodology
  screenshots
  scripts
  mpv
  pipewire
  research
  research/fxsound
  research/dolby
  references
  benchmark
  measurements
  autoeq
  impulse-responses
  .github/workflows
)

REQUIRED_FILES=(
  README.md
  LICENSE
  CHANGELOG.md
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  SECURITY.md
  AUDIO_ROADMAP.md
  .gitignore
  .editorconfig
  docs/INSTALL.md
  docs/PIPEWIRE.md
  docs/MPV.md
  docs/methodology/TEST_PROTOCOL.md
  docs/audio-engine/README.md
  research/FEATURE_MATRIX.md
  presets/README.md
  presets/HISTORY.md
  benchmark/README.md
  .github/workflows/validate-json.yml
)

errors=0

echo "==> Checking directory structure"
for d in "${REQUIRED_DIRS[@]}"; do
  if [[ ! -d "$d" ]]; then
    echo "MISSING DIR: $d"
    errors=$((errors + 1))
  fi
done

echo "==> Checking required files"
for f in "${REQUIRED_FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "MISSING FILE: $f"
    errors=$((errors + 1))
  fi
done

echo "==> Validating preset JSON"
mapfile -t json_files < <(find presets -type f -name '*.json' | sort)
if [[ ${#json_files[@]} -eq 0 ]]; then
  echo "ERROR: no JSON presets found under presets/"
  errors=$((errors + 1))
fi

for f in "${json_files[@]}"; do
  base="$(basename "$f")"
  if [[ ! "$base" =~ ^[a-z0-9]+(-[a-z0-9]+)*\.json$ ]]; then
    echo "BAD NAME (use kebab-case): $f"
    errors=$((errors + 1))
  fi

  if ! python3 -c "
import json, sys
path = sys.argv[1]
with open(path, encoding='utf-8') as fh:
    data = json.load(fh)
if 'output' not in data and 'input' not in data:
    raise SystemExit('missing output/input root key')
section = data.get('output') or data.get('input')
if not isinstance(section, dict):
    raise SystemExit('output/input must be an object')
if 'plugins_order' not in section:
    raise SystemExit('missing plugins_order')
" "$f"; then
    echo "INVALID JSON / SCHEMA: $f"
    errors=$((errors + 1))
  else
    echo "OK  $f"
  fi
done

if [[ "$errors" -ne 0 ]]; then
  echo
  echo "Validation failed with $errors error(s)."
  exit 1
fi

echo
echo "Validation passed (${#json_files[@]} presets)."
