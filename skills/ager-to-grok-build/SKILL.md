---
name: ager-to-grok-build
description: Translate a validated AGER/OKF AgentGraph into a Grok Build plugin (.grok-plugin, Claude-compatible skills, AGENTS.md).
---

# AGER → Grok Build

Compile only. Always emit `.claude-plugin/` **and** `.grok-plugin/`.

1. Locate the AGER bundle.
2. Validate with `ager-validate` if present.
3. `python3 scripts/emit.py --bundle <AGER> --out <OUT>`
4. Report paths. Do not freehand the tree.
