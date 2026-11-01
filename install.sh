#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SKILLS=(
  "odissrea"
  "antirez-cleanroom"
  "telemaco"
  "outis"
  "atena"
  "ermes"
  "penelope"
  "proteo"
  "itaca"
  "ea"
  "ogigia"
  "eolia"
  "scheria"
  "tiresia"
  "demodoco"
)

TARGETS=(
  "$HOME/.gemini/config/skills"
  "$HOME/.claude/skills"
  "$HOME/.config/opencode/skills"
)

for dir in "${TARGETS[@]}"; do
  mkdir -p "$dir"
  for s in "${SKILLS[@]}"; do
    if [ -d "$SCRIPT_DIR/skills/$s" ]; then
      cp -r "$SCRIPT_DIR/skills/$s" "$dir/"
    fi
  done
  echo "[✓] Installed OdissRea pantheon (${SKILLS[*]}) -> $dir"
done

# Merge MCP Server into the existing config
"$(command -v python3 || command -v python)" "$SCRIPT_DIR/mcp/install_mcp_config.py"
echo "✅ OdissRea Clean-Room Suite installation complete. The server path points to this clone: keep it in place."
