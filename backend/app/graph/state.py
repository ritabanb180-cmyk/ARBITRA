"""Shared state passed between graph nodes."""

import operator
from typing import Annotated, TypedDict

from app.agents.base import AgentResult


class GraphState(TypedDict, total=False):
    """State of one pipeline run."""

    query: str
    task_type: str
    # Parallel agent nodes each add one entry; the reducer merges them.
    agent_outputs: Annotated[dict[str, AgentResult], operator.or_]
    selected_agent: str
    confidence: float
    answer: str
    final_answer: str
