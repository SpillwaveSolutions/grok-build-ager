"""AGER IR + sample matching okf-agent-graph sample-ager v0.3.0."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

@dataclass
class Agent:
    id: str
    role: str
    title: str
    description: str
    instructions: str
    tools: list[str] = field(default_factory=list)
    ephemeral: bool = False
    max_workers: int = 5
    record_key: str = ""
    record_mode: str = "append"

@dataclass
class Tool:
    id: str
    title: str
    description: str
    cost_usd: float = 0.0
    rules: list[dict[str, Any]] = field(default_factory=list)

@dataclass
class AgerGraph:
    id: str
    title: str
    description: str
    ager_version: str
    entry: str
    agents: list[Agent]
    tools: list[Tool]
    max_turns: int
    price_budget: float
    deadline_ms: int
    loop_priority: list[str]
    on_goal: str = "return"
    on_exhaust: str = "return_best"

def load_sample() -> AgerGraph:
    return AgerGraph(
        id="parallel-research", title="Parallel research graph",
        description="Orchestrator-workers research with judge and synthesizer.",
        ager_version="0.3.0", entry="lead-researcher", max_turns=6, price_budget=2.5,
        deadline_ms=600000, loop_priority=["goal", "deadline", "price_budget", "max_turns", "no_progress"],
        agents=[
            Agent("lead-researcher", "orchestrator", "Lead researcher", "Plans facets.", "Decompose, spawn, judge, synthesize.", max_workers=5, record_key="orchestrator_plans"),
            Agent("worker", "worker", "Specialist worker", "Isolated doer.", "Structured findings only.", tools=["web_search"], ephemeral=True, record_key="worker_outputs"),
            Agent("judge", "judge", "Quality judge", "Rubric scorer.", "Pass if score >= 0.78.", record_key="judgments"),
            Agent("synthesizer", "synthesizer", "Synthesizer", "Fan-in reduce.", "Merge findings into a report.", record_key="final_report", record_mode="set"),
        ],
        tools=[Tool("web_search", "Web search", "Budgeted search.", 0.002, [{"id": "block-if-budget", "action": "block", "message": "Price budget exhausted"}])],
    )

def load_bundle(path: Path | None) -> AgerGraph:
    return load_sample()
