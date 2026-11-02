"""Common interface for stub agents."""

from abc import ABC, abstractmethod
from typing import TypedDict

from langchain_core.language_models.fake_chat_models import FakeListChatModel


class AgentResult(TypedDict):
    """Output every agent returns."""

    answer: str
    confidence: float


class BaseAgent(ABC):
    """Base class for agents backed by an offline fake chat model."""

    name: str
    confidence: float

    def __init__(self) -> None:
        self.llm = FakeListChatModel(responses=[self.canned_answer()])

    @abstractmethod
    def canned_answer(self) -> str:
        """Return the fixed text the fake model replies with."""

    def run(self, query: str) -> AgentResult:
        """Answer a query using the fake model."""
        reply = self.llm.invoke(query)
        return {"answer": str(reply.content), "confidence": self.confidence}
