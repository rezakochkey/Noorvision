from noorvision.agent import NoorvisionAgent
from noorvision.cycle import run_cycle
from noorvision.memory import Memory, MemoryKind
from noorvision.snapshot import MemorySnapshot


def test_snapshot_changes_after_learning_cycle() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")
    agent.memory_store.add(
        Memory(
            MemoryKind.DECISION,
            "Run experiment",
            "The next step is to validate an explicit hypothesis.",
        )
    )

    before = MemorySnapshot.capture(agent.memory_store)
    result = run_cycle(agent)
    after = MemorySnapshot.capture(agent.memory_store)

    assert result.trace.experiment_executed is True
    assert result.trace.result_memory_created is True
    assert after.total == before.total + 1
    before_counts = dict(before.by_kind)
    after_counts = dict(after.by_kind)
    assert after_counts.get(MemoryKind.RESULT.value, 0) == before_counts.get(MemoryKind.RESULT.value, 0) + 1
