"""Stub vision agent."""

from app.agents.base import BaseAgent


class VisionAgent(BaseAgent):
    """Placeholder for image understanding."""

    name = "vision"
    confidence = 0.70

    def canned_answer(self) -> str:
        return "[vision] stub answer"
