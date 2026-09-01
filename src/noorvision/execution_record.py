"""Immutable record of a task execution."""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class ExecutionRecord:
    """Capture the observable output of executing one evaluation task."""

    task_id: str
    input: object
    actual_output: object
    execution_id: str = field(default_factory=lambda: uuid4().hex)

    def __post_init__(self) -> None:
        if not self.task_id:
            raise ValueError("task_id must not be empty")
        if not self.execution_id:
            raise ValueError("execution_id must not be empty")
