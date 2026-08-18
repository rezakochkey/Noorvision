from noorvision.agent import NoorvisionAgent
from noorvision.cycle_v2 import run_cycle
from noorvision.memory import Memory, MemoryKind


def test_traced_cycle_reports_experiment_and_result() -> None:
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
