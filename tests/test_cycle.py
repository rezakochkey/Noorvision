from noorvision.agent import NoorvisionAgent
from noorvision.cycle import run_cycle


def test_cycle_observes_empty_agent() -> None:
    result = run_cycle(NoorvisionAgent())

    assert result.step.memory_count == 0
    assert result.step.decision.action == "capture_context"


def test_cycle_reflects_captured_context() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")

    result = run_cycle(agent)

    assert result.step.memory_count == 1
    assert result.step.decision.action == "record_decision"
