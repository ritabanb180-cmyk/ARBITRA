"""Common interface for arbitration strategies."""

from abc import ABC, abstractmethod
from typing import TypedDict

from app.agents.base import AgentResult


class ArbitrationResult(TypedDict):
    """Decision produced by a strategy."""

    selected_agent: str
    answer: str
    confidence: float


class ArbitrationStrategy(ABC):
    """Chooses a final answer from the agents' outputs."""

    @abstractmethod
    def arbitrate(
        self, task_type: str, outputs: dict[str, AgentResult]
    ) -> ArbitrationResult:
        """Pick the winning agent output for the given task type."""
