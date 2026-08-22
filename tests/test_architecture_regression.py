from noorvision.agent import NoorvisionAgent
from noorvision.cycle import run_cycle
from noorvision.cycle_v2 import run_cycle as run_traced_cycle
from noorvision.history_service import HistoryService
from noorvision.memory import Memory, MemoryKind


def test_cycle_v2_preserves_experiment_behavior_without_replacing_cycle() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")
    agent.memory_store.add(
        Memory(
            MemoryKind.DECISION,
            "Run experiment",
            "The next step is to run an explicit experiment.",
        )
    )

    legacy_result = run_cycle(agent)
    traced_result = run_traced_cycle(agent)

    assert legacy_result.step.decision.action == "run_next_experiment"
    assert traced_result.step.decision.action == "run_next_experiment"
    assert traced_result.trace.experiment_executed is True
    assert traced_result.trace.result_memory_created is True


def test_history_service_is_importable_alongside_cycle_layers(tmp_path) -> None:
    service = HistoryService(tmp_path / "history.json")
    agent = NoorvisionAgent()

    result = service.run(agent, 1)

    assert result.summary.cycles == 1
    assert len(service.history) == 1
    assert service.latest(1)[0] is result
