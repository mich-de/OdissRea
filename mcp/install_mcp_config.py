#!/usr/bin/env python3
"""Registers odissrea-cleanroom-mcp in the Gemini MCP config, keeping every other server."""

import datetime
import json
import os
import shutil
import sys

SERVER_NAME = "odissrea-cleanroom-mcp"


def merge_config(config_path: str, server_path: str, command: str) -> None:
    config = {}
    if os.path.exists(config_path):
        # utf-8-sig: earlier installer versions wrote a BOM
        with open(config_path, "r", encoding="utf-8-sig") as f:
            config = json.load(f)  # invalid JSON aborts here, leaving the file untouched
        if not isinstance(config, dict) or not isinstance(config.get("mcpServers", {}), dict):
            raise ValueError(f"{config_path}: unexpected structure, not modifying it")
        stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        shutil.copy2(config_path, f"{config_path}.{stamp}.bak")

    config.setdefault("mcpServers", {})[SERVER_NAME] = {
        "command": command,
        "args": [server_path],
        "env": {"PYTHONIOENCODING": "utf-8"},
    }

    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    tmp_path = config_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(config, f, indent=2)
        f.write("\n")
    os.replace(tmp_path, config_path)


def main() -> int:
    config_path = os.path.join(os.path.expanduser("~"), ".gemini", "config", "mcp_config.json")
    server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "odissrea_cleanroom_server.py").replace("\\", "/")
    command = "python" if os.name == "nt" else "python3"
    try:
        merge_config(config_path, server_path, command)
    except (OSError, ValueError) as e:
        print(f"[!] MCP config not changed: {e}", file=sys.stderr)
        return 1
    print(f"[OK] Configured MCP Server -> {config_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
