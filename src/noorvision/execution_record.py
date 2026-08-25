"""Immutable record of a task execution."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionRecord:
    """Capture the observable output of executing one evaluation task."""

    task_id: str
    input: object
    actual_output: object

    def __post_init__(self) -> None:
        if not self.task_id:
            raise ValueError("task_id must not be empty")
