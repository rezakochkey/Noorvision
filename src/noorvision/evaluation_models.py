"""Shared immutable models for NOORVISION evaluation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .execution_record import ExecutionRecord


@dataclass(frozen=True, slots=True)
class EvaluationCase:
    """A deterministic evaluation case."""

    case_id: str
    expected: Any
    actual: Any


@dataclass(frozen=True, slots=True)
class EvaluationOutcome:
    """The outcome of evaluating one case."""

    case_id: str
    passed: bool
    score: float
    reason: str
    execution: "ExecutionRecord | None" = None
