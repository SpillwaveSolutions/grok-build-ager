# Hosts — grok-build-ager

A host gets a **manifest**, never a fork.

| Host | What it reads |
| --- | --- |
| Agent Plugins 1.0 | `plugin.json` + `skills/` |
| Grok Build | Claude layout + `.grok-plugin/` |
| Claude Code | `.claude-plugin/` |
| Codex | `.codex-plugin/` |
| Cursor | Agent Plugins 1.0 + `hosts/cursor/SKILL.md` |
