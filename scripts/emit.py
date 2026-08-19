#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from ir import load_bundle

def write(out, rel, content):
    dest = out / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content if content.endswith("\n") else content + "\n", encoding="utf-8")
    return dest

def emit(graph, out):
    written = []
    ident = {"name": graph.id, "version": "0.1.0", "description": f"Compiled AGER graph: {graph.title}", "ager_version": graph.ager_version}
    written.append(write(out, "plugin.json", json.dumps(ident, indent=2)))
    written.append(write(out, ".claude-plugin/plugin.json", json.dumps(ident, indent=2)))
    written.append(write(out, ".grok-plugin/marketplace.json", json.dumps({"name": f"{graph.id}-marketplace", "version": "0.1.0", "plugins": [{"name": graph.id, "source": ".", "compatibility": {"claude_plugin": True, "zero_config": True}}]}, indent=2)))
    lead = next(a for a in graph.agents if a.role == "orchestrator")
    written.append(write(out, "AGENTS.md", f"# {graph.title}\n\nAGER {graph.ager_version} for Grok Build. Entry `{graph.entry}`. max_turns={graph.max_turns} price=${graph.price_budget}. Use /ager-run.\n"))
    written.append(write(out, "skills/ager-run/SKILL.md", f"---\nname: ager-run\ndescription: Run {graph.id}\n---\n\n# {graph.title}\n\nEntry {lead.title}. Stop on goal / deadline / ${graph.price_budget} / {graph.max_turns} turns.\n"))
    for agent in graph.agents:
        written.append(write(out, f"skills/{agent.id}/SKILL.md", f"---\nname: {agent.id}\ndescription: {agent.description}\n---\n\n# {agent.title}\n\n{agent.instructions}\n"))
    written.append(write(out, f"agents/{lead.id}.md", f"---\nname: {lead.id}\ndescription: {lead.description}\n---\n\n# {lead.title}\n\n{lead.instructions}\n"))
    written.append(write(out, "commands/ager-run.md", f"---\nname: ager-run\ndescription: Run {graph.id}\n---\n\nFollow ager-run.\n"))
    return written

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--bundle", type=Path)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    for w in emit(load_bundle(args.bundle), args.out):
        print(w)

if __name__ == "__main__":
    main()
