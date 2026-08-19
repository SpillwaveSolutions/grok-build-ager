---
name: ager-to-grok-build
description: Translate a validated AGER/OKF AgentGraph into a Grok Build plugin (.grok-plugin, Claude-compatible skills, AGENTS.md).
---

# AGER → Grok Build

Compile only. Authoring is `okf-agent-graph`.

## Mapping

| AGER | Grok Build |
| --- | --- |
| AgentGraph | `.grok-plugin/marketplace.json` + `AGENTS.md` |
| OrchestratorAgent | `agents/<id>.md` + skill |
| Worker / Judge / Synthesizer | `skills/<id>/SKILL.md` |
| LoopPolicy | `skills/ager-run/SKILL.md` |
| Tool + ToolRule | skill tool section; no invented MCP |
| ScratchPad | `runs/<id>/scratchpad/` keys |

Grok Build consumes Claude plugin files. Always emit `.claude-plugin/` **and** `.grok-plugin/`.

## Steps

1. Locate the AGER bundle.
2. Validate with `ager-validate` if `okf-agent-graph` is present.
3. Run:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/emit.py --bundle <AGER_ROOT> --out <OUT>
```

4. Report paths. Do not freehand the tree.
5. Never claim production-ready without tests.

## References

- `references/mapping.md`
