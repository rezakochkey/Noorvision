from noorvision.agent import NoorvisionAgent
from noorvision.cycle import run_cycle


def test_cycle_observes_empty_agent() -> None:
    agent = NoorvisionAgent()

    result = run_cycle(agent)

    assert result.step.memory_count == 0
    assert result.step.decision.action == "capture_context"
    assert result.action_result.action == "capture_context"
    assert result.action_result.memory is not None
    assert len(agent.memory_store) == 1


def test_cycle_reflects_captured_context() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")

    result = run_cycle(agent)

    assert result.step.memory_count == 1
    assert result.step.decision.action == "record_decision"
    assert result.action_result.action == "record_decision"
