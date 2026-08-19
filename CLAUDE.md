# CLAUDE.md — grok-build-ager

Claude Code conventions. Grok Build and Cursor also read this file.

## What this is

A **translator**. Author graphs with `okf-agent-graph`. This plugin compiles.

Command: `/ager-to-grok-build`

Prefer:

```bash
python3 scripts/emit.py --bundle <AGER> --out ./generated
```

## Hosts

One tree, five surfaces. See docs/HOSTS.md and docs/CURSOR.md.

- Agent Plugins 1.0 — root plugin.json
- Claude Code — .claude-plugin/
- Grok Build — Claude layout + .grok-plugin/
- Codex — .codex-plugin/
- Cursor — .cursor-plugin/ + hosts/cursor/

## Rules

- Do not invent agents
- LoopPolicy order: goal, deadline, price, max_turns, no_progress
- Never claim production-ready without tests
