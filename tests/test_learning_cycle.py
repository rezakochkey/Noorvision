from noorvision.agent import NoorvisionAgent
from noorvision.cycle import run_cycle
from noorvision.memory import MemoryKind


def test_learning_cycle_records_experiment_result() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")

    # First cycle records the next decision; the following cycle can act on it.
    first = run_cycle(agent)
    assert first.step.decision.action == "record_decision"

    agent.memory_store.add(
        __import__("noorvision.memory", fromlist=["Memory"]).Memory(
            MemoryKind.DECISION,
            "Run experiment",
            "The next step is to run an explicit experiment.",
        )
    )

    second = run_cycle(agent)

    assert second.step.decision.action == "run_next_experiment"
    assert any(
        memory.kind is MemoryKind.RESULT
        for memory in agent.memory_store.list()
    )
