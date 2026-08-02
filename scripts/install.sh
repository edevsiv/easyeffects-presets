#!/usr/bin/env bash
# Install EasyEffects output presets from this repository.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'EOF'
Usage: ./scripts/install.sh [--flatpak|--native|--auto] [--dry-run]

Installs all JSON presets from presets/*/ into the EasyEffects output directory.

Options:
  --auto      Detect Flatpak vs native (default)
  --flatpak   Force Flatpak config path
  --native    Force native XDG paths
  --dry-run   Show actions without copying
  -h, --help  Show this help
EOF
}

MODE="auto"
DRY_RUN=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --auto) MODE="auto" ;;
    --flatpak) MODE="flatpak" ;;
    --native) MODE="native" ;;
    --dry-run) DRY_RUN=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1"; usage; exit 1 ;;
  esac
  shift
done

detect_target() {
  local flatpak_share flatpak_cfg native_share native_cfg
  # EasyEffects 8+ Flatpak uses XDG_DATA_HOME inside the sandbox (config/ triggers migrate→trash).
  flatpak_share="${HOME}/.var/app/com.github.wwmm.easyeffects/data/easyeffects/output"
  flatpak_cfg="${HOME}/.var/app/com.github.wwmm.easyeffects/config/easyeffects/output"
  # Newer EasyEffects prefers XDG_DATA_HOME; older used XDG_CONFIG_HOME.
  native_share="${XDG_DATA_HOME:-$HOME/.local/share}/easyeffects/output"
  native_cfg="${XDG_CONFIG_HOME:-$HOME/.config}/easyeffects/output"

  case "$MODE" in
    flatpak)
      if [[ -d "$(dirname "$flatpak_share")" ]] || [[ ! -d "$(dirname "$flatpak_cfg")" ]]; then
        echo "$flatpak_share"
      else
        echo "$flatpak_cfg"
      fi
      return
      ;;
    native)
      if [[ -d "$(dirname "$native_share")" ]] || [[ ! -d "$(dirname "$native_cfg")" ]]; then
        echo "$native_share"
      else
        echo "$native_cfg"
      fi
      return
      ;;
  esac

  if command -v flatpak >/dev/null 2>&1 && flatpak info com.github.wwmm.easyeffects >/dev/null 2>&1; then
    if [[ -d "$(dirname "$flatpak_share")" ]]; then
      echo "$flatpak_share"
    else
      echo "$flatpak_cfg"
    fi
  elif [[ -d "$(dirname "$native_share")" ]]; then
    echo "$native_share"
  else
    echo "$native_cfg"
  fi
}

TARGET="$(detect_target)"
echo "Target directory: $TARGET"

if [[ "$DRY_RUN" -eq 0 ]]; then
  mkdir -p "$TARGET"
fi

count=0
while IFS= read -r -d '' src; do
  dest="$TARGET/$(basename "$src")"
  echo "  $(basename "$src") -> $dest"
  if [[ "$DRY_RUN" -eq 0 ]]; then
    cp -f "$src" "$dest"
  fi
  count=$((count + 1))
done < <(find "$ROOT/presets" -type f -name '*.json' -print0 | sort -z)

echo
if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "Dry-run complete ($count presets)."
else
  echo "Installed $count presets."
  echo "Open EasyEffects → Presets and reload / select a preset."
fi
