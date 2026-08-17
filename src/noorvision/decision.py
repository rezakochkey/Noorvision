"""Small deterministic decision primitives for Noorvision."""

from dataclasses import dataclass

from .memory import Memory, MemoryKind


@dataclass(frozen=True, slots=True)
class Decision:
    """A proposed next action derived from available memory."""

    action: str
    reason: str


def next_action(memories: list[Memory]) -> Decision:
    """Choose the next useful action using simple, inspectable rules."""
    if not memories:
        return Decision(
            action="capture_context",
            reason="No memory is available yet; capture the current project context first.",
        )

    if not any(memory.kind is MemoryKind.PROJECT for memory in memories):
        return Decision(
            action="define_project",
            reason="Memory exists, but no project context has been recorded.",
        )

    if not any(memory.kind is MemoryKind.DECISION for memory in memories):
        return Decision(
            action="record_decision",
            reason="Project context exists; record an important decision before expanding the system.",
        )

    return Decision(
        action="run_next_experiment",
        reason="Project context and at least one decision are recorded; validate the next hypothesis.",
    )
