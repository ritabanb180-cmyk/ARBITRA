"""Request and response models for the chat endpoint."""

from pydantic import BaseModel, Field


class AgentOutput(BaseModel):
    """Answer and confidence reported by a single agent."""

    answer: str
    confidence: float = Field(ge=0.0, le=1.0)


class ChatRequest(BaseModel):
    """Incoming user message."""

    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    """Final arbitrated answer plus the per-agent outputs."""

    answer: str
    confidence: float
    task_type: str
    selected_agent: str
    agent_outputs: dict[str, AgentOutput]
