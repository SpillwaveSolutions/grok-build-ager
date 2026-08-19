# grok-build-ager

AGER translator. Compiles a validated bundle into **one tree** every host can load.

A host gets a manifest, never a fork. See [docs/HOSTS.md](docs/HOSTS.md).

| Host | Reads |
| --- | --- |
| **Agent Plugins 1.0** | [`plugin.json`](plugin.json) + `skills/` |
| **Grok Build** | Claude layout (zero-config) + `.grok-plugin/` |
| **Claude Code** | `.claude-plugin/` |
| **Codex** | `.codex-plugin/` (`$ager-to-grok-build`) |
| **Cursor** | Agent Plugins 1.0 + [hosts/cursor/SKILL.md](hosts/cursor/SKILL.md) |

```bash
python3 scripts/emit.py --bundle path/to/sample-ager --out ./generated
```

## License

MIT
