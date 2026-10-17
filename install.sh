#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SKILLS=(
  "odissrea"
  "outis"
  "atena"
  "ermes"
  "penelope"
  "proteo"
  "itaca"
  "t-800"
  "eritrea"
)

TARGETS=(
  "$HOME/.gemini/config/skills"
  "$HOME/.claude/skills"
  "$HOME/.config/opencode/skills"
)

for dir in "${TARGETS[@]}"; do
  mkdir -p "$dir"
  for s in "${SKILLS[@]}"; do
    cp -r "$SCRIPT_DIR/skills/$s" "$dir/"
  done
  echo "[✓] Installed OdissRea pantheon (${SKILLS[*]}) -> $dir"
done
