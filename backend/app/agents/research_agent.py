"""Stub research agent."""

from app.agents.base import BaseAgent


class ResearchAgent(BaseAgent):
    """Placeholder for information lookup and reasoning."""

    name = "research"
    confidence = 0.75

    def canned_answer(self) -> str:
        return "[research] stub answer"
