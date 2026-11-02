"""Trust-weighted arbitration (not implemented yet)."""

from app.agents.base import AgentResult
from app.arbitration.base import ArbitrationResult, ArbitrationStrategy


class TrustWeightingStrategy(ArbitrationStrategy):
    """Weight each agent's answer by a learned trust score."""

    def arbitrate(
        self, task_type: str, outputs: dict[str, AgentResult]
    ) -> ArbitrationResult:
        # TODO: implement trust-weighted arbitration.
        raise NotImplementedError("TODO: trust_weighting strategy is not implemented yet")
