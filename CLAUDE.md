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

<!-- worklog:policy:start -->
## WikiTicket SDD (worklog)

This plugin tracks implementation with [WikiTicket SDD](https://github.com/SpillwaveSolutions/wiki_ticket_sdd).

- Install the `worklog` plugin from `SpillwaveSolutions/wiki_ticket_sdd` (Claude Code, Grok Build, Codex, Cursor).
- Config lives in `.work/config.yml`. Event log is `.work/todo.jsonl`.
- Every plan MUST end by running `worklog plan-capture`.
- Work discovered mid-flight: `worklog add --unplanned --discovered-during <item>` BEFORE doing the work.
- Never hand-edit `.work/*.jsonl` (use `worklog`) or `docs/roadmap.md` (generated).
- After changing work items, run `worklog roadmap-render` and commit the log and roadmap together.
- CLI: `worklog` on PATH, or `python3 <wiki_ticket_sdd>/bin/worklog`.
<!-- worklog:policy:end -->

