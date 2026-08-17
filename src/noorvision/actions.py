"""Explicit, safe actions for Noorvision's local execution cycle."""

from dataclasses import dataclass

from .memory import Memory, MemoryKind
from .memory_store import MemoryStore


@dataclass(frozen=True, slots=True)
class ActionResult:
    action: str
    memory: Memory | None = None


def execute_action(store: MemoryStore, action: str) -> ActionResult:
    """Execute only known local actions; unknown actions are rejected."""
    if action == "capture_context":
        memory = store.add(
            Memory(
                MemoryKind.PROJECT,
                "Initial context",
                "Context capture requested by the Noorvision decision loop.",
            )
        )
        return ActionResult(action=action, memory=memory)

    if action in {"define_project", "record_decision", "run_next_experiment"}:
        return ActionResult(action=action)

    raise ValueError(f"unknown action: {action}")
