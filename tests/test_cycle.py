from noorvision.agent import NoorvisionAgent
from noorvision.cycle import run_cycle
from noorvision.memory import Memory, MemoryKind


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


def test_cycle_traces_experiment_and_result() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")
    agent.memory_store.add(
        Memory(
            MemoryKind.DECISION,
            "Run experiment",
            "The next step is to run an explicit experiment.",
        )
    )

    result = run_cycle(agent)

    assert result.step.decision.action == "run_next_experiment"
    assert result.trace.experiment_executed is True
    assert result.trace.result_memory_created is True
