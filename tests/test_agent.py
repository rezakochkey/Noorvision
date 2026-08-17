from noorvision.agent import NoorvisionAgent
from noorvision.memory import Memory, MemoryKind
from noorvision.memory_store import MemoryStore


def test_agent_observes_empty_workspace() -> None:
    step = NoorvisionAgent().observe()

    assert step.memory_count == 0
    assert step.decision.action == "capture_context"


def test_agent_uses_current_memory_for_decision() -> None:
    store = MemoryStore(
        [Memory(MemoryKind.PROJECT, "Noorvision", "Initial project context")]
    )

    step = NoorvisionAgent(store).observe()

    assert step.memory_count == 1
    assert step.decision.action == "record_decision"
