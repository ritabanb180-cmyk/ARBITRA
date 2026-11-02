import pytest
from fastapi.testclient import TestClient

from app.arbitration import STRATEGIES, get_strategy
from app.graph.builder import build_graph
from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_full_graph_run() -> None:
    state = build_graph("rule_based").invoke({"query": "Fix this python bug"})
    assert state["task_type"] == "coding"
    assert set(state["agent_outputs"]) == {"vision", "audio", "research", "coding"}
    assert state["selected_agent"] == "coding"
    assert state["final_answer"] == state["agent_outputs"]["coding"]["answer"]


def test_chat_endpoint() -> None:
    response = client.post("/api/v1/chat", json={"message": "What is in this image?"})
    assert response.status_code == 200
    body = response.json()
    assert body["task_type"] == "vision"
    assert body["selected_agent"] == "vision"


def test_unknown_strategy_raises_clear_error() -> None:
    with pytest.raises(ValueError, match="Unknown arbitration strategy 'nope'"):
        get_strategy("nope")


@pytest.mark.parametrize("name", ["trust_weighting", "calibration", "meta_agent"])
def test_unimplemented_strategies_raise_todo(name: str) -> None:
    strategy = get_strategy(name)
    with pytest.raises(NotImplementedError, match="TODO"):
        strategy.arbitrate("research", {})


def test_factory_covers_all_strategies() -> None:
    assert set(STRATEGIES) == {"rule_based", "trust_weighting", "calibration", "meta_agent"}
