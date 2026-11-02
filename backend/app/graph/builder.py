"""LangGraph pipeline: router -> agents (parallel) -> arbitration -> synthesizer."""

from functools import lru_cache

from langgraph.graph import END, START, StateGraph

from app.agents import AudioAgent, BaseAgent, CodingAgent, ResearchAgent, VisionAgent
from app.arbitration import get_strategy
from app.core.config import get_settings
from app.graph.state import GraphState

KEYWORDS: dict[str, tuple[str, ...]] = {
    "vision": ("image", "photo", "picture", "video", "diagram"),
    "audio": ("audio", "sound", "speech", "music", "voice"),
    "coding": ("code", "python", "bug", "function", "script"),
}


def route(state: GraphState) -> GraphState:
    """Classify the query into a task type by keyword."""
    query = state["query"].lower()
    for task_type, words in KEYWORDS.items():
        if any(word in query for word in words):
            return {"task_type": task_type}
    return {"task_type": "research"}


def make_agent_node(agent: BaseAgent):
    """Wrap an agent as a graph node that adds its result to the state."""

    def node(state: GraphState) -> GraphState:
        return {"agent_outputs": {agent.name: agent.run(state["query"])}}

    return node


def make_arbitration_node(strategy_name: str):
    """Build the node that applies the configured arbitration strategy."""
    strategy = get_strategy(strategy_name)

    def node(state: GraphState) -> GraphState:
        decision = strategy.arbitrate(state["task_type"], state["agent_outputs"])
        return {
            "selected_agent": decision["selected_agent"],
            "answer": decision["answer"],
            "confidence": decision["confidence"],
        }

    return node


def synthesize(state: GraphState) -> GraphState:
    """Produce the final answer from the arbitrated one."""
    return {"final_answer": state["answer"]}


def build_graph(strategy_name: str):
    """Compile the pipeline graph using the named arbitration strategy."""
    agents: list[BaseAgent] = [
        VisionAgent(),
        AudioAgent(),
        ResearchAgent(),
        CodingAgent(),
    ]
    graph = StateGraph(GraphState)
    graph.add_node("router", route)
    graph.add_node("arbitration", make_arbitration_node(strategy_name))
    graph.add_node("synthesizer", synthesize)
    graph.add_edge(START, "router")
    for agent in agents:
        graph.add_node(agent.name, make_agent_node(agent))
        graph.add_edge("router", agent.name)
    graph.add_edge([agent.name for agent in agents], "arbitration")
    graph.add_edge("arbitration", "synthesizer")
    graph.add_edge("synthesizer", END)
    return graph.compile()


@lru_cache
def get_graph():
    """Return the compiled graph for the configured strategy."""
    return build_graph(get_settings().arbitration_strategy)
