---
name: cursor-grok-build-ager
description: Bind a Cursor agent to grok-build-ager. Cursor loads Agent Plugins 1.0 (plugin.json + skills/).
---

# Cursor / grok-build-ager

1. Identity: `cursor/grok-build-ager`
2. Cursor reads root `plugin.json` + `skills/`.
3. `python3 scripts/emit.py --bundle <AGER> --out <OUT>`
