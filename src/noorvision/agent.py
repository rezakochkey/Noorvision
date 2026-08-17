"""A small orchestration loop for Noorvision's inspectable reasoning core."""

from dataclasses import dataclass

from .decision import Decision, next_action
from .memory import Memory
from .memory_store import MemoryStore


@dataclass(frozen=True, slots=True)
class AgentStep:
    """One observable step taken by the Noorvision core."""

    decision: Decision
    memory_count: int


class NoorvisionAgent:
    """Coordinate memory and deterministic decision-making without external services."""

    def __init__(self, memory_store: MemoryStore | None = None) -> None:
        self.memory_store = memory_store or MemoryStore()

    def observe(self) -> AgentStep:
        """Inspect current memory and propose the next action."""
        memories: list[Memory] = self.memory_store.list()
        return AgentStep(
            decision=next_action(memories),
            memory_count=len(memories),
        )
