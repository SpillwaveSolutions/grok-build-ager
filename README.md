# grok-build-ager

AGER → **Grok Build** translator plugin.

Grok Build loads Claude plugin layout with zero config. Identity is pinned in `.grok-plugin/marketplace.json`.

Author graphs with [`okf-agent-graph`](https://github.com/SpillwaveSolutions/okf-agent-graph). This plugin only compiles.

## Use

```
/ager-to-grok-build
```

```bash
python3 scripts/emit.py --bundle path/to/sample-ager --out ./generated/grok-build
```

## License

MIT
