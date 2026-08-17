"""In-memory storage for Noorvision memory objects."""

from collections.abc import Iterable

from .memory import Memory, MemoryKind


class MemoryStore:
    """A small deterministic store for the current process."""

    def __init__(self, memories: Iterable[Memory] = ()) -> None:
        self._memories: dict[str, Memory] = {str(memory.id): memory for memory in memories}

    def add(self, memory: Memory) -> Memory:
        self._memories[str(memory.id)] = memory
        return memory

    def get(self, memory_id: str) -> Memory | None:
        return self._memories.get(memory_id)

    def list(self, kind: MemoryKind | None = None) -> list[Memory]:
        memories = self._memories.values()
        if kind is not None:
            memories = (memory for memory in memories if memory.kind is kind)
        return list(memories)

    def __len__(self) -> int:
        return len(self._memories)
