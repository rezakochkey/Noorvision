"""Shared immutable models for NOORVISION evaluation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


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
