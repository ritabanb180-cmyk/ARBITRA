"""Stub audio agent."""

from app.agents.base import BaseAgent


class AudioAgent(BaseAgent):
    """Placeholder for audio understanding."""

    name = "audio"
    confidence = 0.65

    def canned_answer(self) -> str:
        return "[audio] stub answer"
