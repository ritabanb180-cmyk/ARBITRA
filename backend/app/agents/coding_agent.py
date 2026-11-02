"""Stub coding agent."""

from app.agents.base import BaseAgent


class CodingAgent(BaseAgent):
    """Placeholder for code generation and debugging."""

    name = "coding"
    confidence = 0.80

    def canned_answer(self) -> str:
        return "[coding] stub answer"
