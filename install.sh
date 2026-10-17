#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

TARGETS=(
  "$HOME/.gemini/config/skills"
  "$HOME/.claude/skills"
  "$HOME/.config/opencode/skills"
)

for dir in "${TARGETS[@]}"; do
  mkdir -p "$dir"
  cp -r "$SCRIPT_DIR/skills/t-800" "$dir/"
  cp -r "$SCRIPT_DIR/skills/eritrea" "$dir/"
  echo "[✓] Installed t-800 & eritrea -> $dir"
done
