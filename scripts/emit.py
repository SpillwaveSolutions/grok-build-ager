#!/usr/bin/env python3
"""Emit a multi-host plugin from an AGER bundle.

Output is Agent Plugins 1.0 + Claude Code + Grok Build + Codex + Cursor.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ir import AgerGraph, load_bundle
from layout import host_manifests, write


def emit(graph: AgerGraph, out: Path) -> list[Path]:
    written = host_manifests(
        out,
        name=graph.id,
        title=graph.title,
        description=f"Compiled AGER graph: {graph.title}",
        version="0.1.0",
        ager_version=graph.ager_version,
        keywords=["ager", "okf", "compiled-graph", "claude-code", "grok-build", "codex", "cursor"],
        default_prompts=[
            f"Run AGER graph {graph.id} via /ager-run or $ager-run.",
            f"Entry {graph.entry}. Honor LoopPolicy. Do not invent agents.",
        ],
    )
    lead = next(a for a in graph.agents if a.role == "orchestrator")
    written.append(
        write(
            out,
            "AGENTS.md",
            f"""# AGENTS.md — {graph.title}

Compiled AGER {graph.ager_version}. Multi-host: Agent Plugins 1.0, Claude Code,
Grok Build, Codex, Cursor.

Entry: `{graph.entry}`. LoopPolicy: {' → '.join(graph.loop_priority)}.
max_turns={graph.max_turns}  price=${graph.price_budget}  deadline_ms={graph.deadline_ms}

Use `/ager-run` or `$ager-run`. Do not invent extra agents.
""",
        )
    )
    written.append(
        write(
            out,
            f"agents/{lead.id}.md",
            f"""---
name: {lead.id}
description: {lead.description}
---

# {lead.title}

{lead.instructions}

Honor `skills/ager-run/SKILL.md`. Record to `{lead.record_key}`.
""",
        )
    )
    written.append(
        write(
            out,
            "skills/ager-run/SKILL.md",
            f"""---
name: ager-run
description: Execute compiled AGER graph {graph.id} on any host.
---

# Run {graph.title}

Entry: **{lead.title}** (`{lead.id}`).

Evaluate after each outer turn, in order:

1. **goal** — stop if judgment.pass
2. **deadline** — {graph.deadline_ms} ms → `{graph.on_exhaust}`
3. **price** — ${graph.price_budget} USD → `{graph.on_exhaust}`
4. **max_turns** — {graph.max_turns} → `{graph.on_exhaust}`
5. **no_progress** — score window 3, min_delta 0.02 → `{graph.on_exhaust}`

Hosts do not meter USD. Track an estimate and stop.
ScratchPad keys only. No full transcripts.
""",
        )
    )
    for agent in graph.agents:
        tools = ", ".join(agent.tools) or "none"
        written.append(
            write(
                out,
                f"skills/{agent.id}/SKILL.md",
                f"""---
name: {agent.id}
description: {agent.description}
---

# {agent.title}

Role: `{agent.role}`

{agent.instructions}

Tools: {tools}
Record: `{agent.record_mode}` → `{agent.record_key or agent.id}`
""",
            )
        )
    written.append(
        write(
            out,
            "commands/ager-run.md",
            f"""---
name: ager-run
description: Run compiled AGER graph {graph.id}.
---

Follow **ager-run** and orchestrator `{lead.id}`.
Codex: `$ager-run`. Claude / Grok: `/ager-run`.
""",
        )
    )
    written.append(
        write(
            out,
            "docs/CURSOR.md",
            f"""# Cursor — {graph.title}

This compiled graph is an [Agent Plugins 1.0](https://agent-plugins.org/specification)
package. Cursor loads `plugin.json` + `skills/`.

```
/plugin install {graph.id}
```

or link this directory into the workspace plugin path.
Identity: `cursor/{graph.id}`.
""",
        )
    )
    return written


def main() -> None:
    p = argparse.ArgumentParser(prog="ager-emit")
    p.add_argument("--bundle", type=Path)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    written = emit(load_bundle(args.bundle), args.out)
    print(f"wrote {len(written)} files to {args.out}")
    for w in written:
        print(" ", w)


if __name__ == "__main__":
    main()
