from noorvision.memory import Memory, MemoryKind
from noorvision.memory_store import MemoryStore


def test_store_adds_and_gets_memory() -> None:
    store = MemoryStore()
    memory = Memory(MemoryKind.PROJECT, "Noorvision", "Initial project scaffold")

    assert store.add(memory) is memory
    assert store.get(str(memory.id)) is memory
    assert len(store) == 1


def test_store_filters_by_kind() -> None:
    project = Memory(MemoryKind.PROJECT, "Project", "A project")
    decision = Memory(MemoryKind.DECISION, "Decision", "A decision")
    store = MemoryStore([project, decision])

    assert store.list(MemoryKind.PROJECT) == [project]
    assert store.list(MemoryKind.DECISION) == [decision]
    assert store.list() == [project, decision]


def test_store_returns_none_for_unknown_id() -> None:
    assert MemoryStore().get("missing") is None
