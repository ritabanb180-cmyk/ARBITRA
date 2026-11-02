"""Stub agents."""

from app.agents.audio_agent import AudioAgent
from app.agents.base import AgentResult, BaseAgent
from app.agents.coding_agent import CodingAgent
from app.agents.research_agent import ResearchAgent
from app.agents.vision_agent import VisionAgent

__all__ = [
    "AgentResult",
    "AudioAgent",
    "BaseAgent",
    "CodingAgent",
    "ResearchAgent",
    "VisionAgent",
]
