"""Inspectable memory snapshots for Noorvision runs."""

from dataclasses import dataclass

from .memory import Memory, MemoryKind
from .memory_store import MemoryStore


@dataclass(frozen=True, slots=True)
class MemorySnapshot:
    """Immutable summary of memory state at a point in time."""

    total: int
    by_kind: tuple[tuple[str, int], ...]

    @classmethod
    def capture(cls, store: MemoryStore) -> "MemorySnapshot":
        counts: dict[str, int] = {}
        for memory in store.list():
            key = memory.kind.value if isinstance(memory.kind, MemoryKind) else str(memory.kind)
            counts[key] = counts.get(key, 0) + 1
        return cls(total=len(store), by_kind=tuple(sorted(counts.items())))
