"""Deterministic evaluation engine for NOORVISION evaluation cases."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class EvaluationOutcome:
    """The outcome of evaluating one case."""

    case_id: str
    passed: bool
    score: float
    reason: str


@dataclass(frozen=True, slots=True)
class EvaluationCase:
    """A deterministic evaluation case."""

    case_id: str
    expected: Any
    actual: Any


Evaluator = Callable[[EvaluationCase], EvaluationOutcome]


def evaluate_case(case: EvaluationCase) -> EvaluationOutcome:
    """Evaluate a case using exact value comparison."""
    if not case.case_id:
        raise ValueError("case_id must not be empty")

    passed = case.actual == case.expected
    return EvaluationOutcome(
        case_id=case.case_id,
        passed=passed,
        score=1.0 if passed else 0.0,
        reason="exact match" if passed else "actual value does not match expected value",
    )
