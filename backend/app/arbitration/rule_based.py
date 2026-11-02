"""Baseline strategy: fixed agent priority per task type."""

from app.agents.base import AgentResult
from app.arbitration.base import ArbitrationResult, ArbitrationStrategy

PRIORITY: dict[str, list[str]] = {
    "vision": ["vision", "research", "coding", "audio"],
    "audio": ["audio", "research", "coding", "vision"],
    "coding": ["coding", "research", "vision", "audio"],
    "research": ["research", "coding", "vision", "audio"],
}


class RuleBasedStrategy(ArbitrationStrategy):
    """Select the first available agent in the task type's priority list."""

    def arbitrate(
        self, task_type: str, outputs: dict[str, AgentResult]
    ) -> ArbitrationResult:
        order = PRIORITY.get(task_type, PRIORITY["research"])
        for name in order:
            if name in outputs:
                return {"selected_agent": name, **outputs[name]}
        raise ValueError("No agent outputs to arbitrate")
