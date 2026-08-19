---
name: ager-to-grok-build
description: Compile an AGER AgentGraph into a Grok Build plugin.
---

Follow the **ager-to-grok-build** skill completely.

1. Load the skill.
2. Validate the AGER bundle when `okf-agent-graph` is available.
3. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/emit.py --bundle <AGER> --out <OUT>`.
4. Report created paths.
