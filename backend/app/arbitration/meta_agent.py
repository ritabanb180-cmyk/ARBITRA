"""Meta-agent arbitration (not implemented yet)."""

from app.agents.base import AgentResult
from app.arbitration.base import ArbitrationResult, ArbitrationStrategy


class MetaAgentStrategy(ArbitrationStrategy):
    """Let a dedicated meta-agent judge between the agents' answers."""

    def arbitrate(
        self, task_type: str, outputs: dict[str, AgentResult]
    ) -> ArbitrationResult:
        # TODO: implement meta-agent arbitration.
        raise NotImplementedError("TODO: meta_agent strategy is not implemented yet")
