from noorvision.agent import NoorvisionAgent
from noorvision.cycle import run_cycle
from noorvision.memory import MemoryKind
from noorvision.snapshot import MemorySnapshot


def test_snapshot_changes_after_learning_cycle() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")

    before = MemorySnapshot.capture(agent.memory_store)
    run_cycle(agent)

    after = MemorySnapshot.capture(agent.memory_store)

    assert after.total > before.total
    before_counts = dict(before.by_kind)
    after_counts = dict(after.by_kind)
    assert after_counts.get(MemoryKind.DECISION.value, 0) >= before_counts.get(MemoryKind.DECISION.value, 0)
