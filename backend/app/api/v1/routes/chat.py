"""Chat endpoint that runs the multi-agent graph."""

from fastapi import APIRouter

from app.graph.builder import get_graph
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Run the LangGraph pipeline for a user message."""
    state = get_graph().invoke({"query": request.message})
    return ChatResponse(
        answer=state["final_answer"],
        confidence=state["confidence"],
        task_type=state["task_type"],
        selected_agent=state["selected_agent"],
        agent_outputs=state["agent_outputs"],
    )
