"""Task definition for deterministic NOORVISION evaluations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class EvaluationTask:
    """A reproducible task definition presented to an evaluated system."""

    task_id: str
    input: Any
    expected_output: Any

    def __post_init__(self) -> None:
        if not self.task_id:
            raise ValueError("task_id must not be empty")
