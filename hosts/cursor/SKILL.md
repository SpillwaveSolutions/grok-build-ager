---
name: cursor-grok-build-ager
description: Bind a Cursor agent to grok-build-ager. Compile AGER graphs. Do not author graphs.
---

# Cursor / grok-build-ager

Follow `docs/CURSOR.md` and `docs/HOSTS.md`.

1. Identity: `cursor/grok-build-ager`.
2. Local Cursor may `/plugin install grok-build-ager`.
3. Compile with `python3 scripts/emit.py --bundle <AGER> --out <OUT>`.
4. Never invent agents. Never write a new AGER graph (that is `okf-agent-graph`).
