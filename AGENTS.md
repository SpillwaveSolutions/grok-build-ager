# AGENTS.md — grok-build-ager

Multi-host translator. Author graphs with `okf-agent-graph`.

- Agent Plugins 1.0: `plugin.json` + `skills/`
- Grok Build: Claude layout + `.grok-plugin/`
- Claude Code: `.claude-plugin/`
- Codex: `.codex-plugin/`
- Cursor: `hosts/cursor/SKILL.md`

`/ager-to-grok-build` · `$ager-to-grok-build` · `python3 scripts/emit.py`

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

