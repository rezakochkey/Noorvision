"""Deterministic evaluation engine for NOORVISION evaluation cases."""

from __future__ import annotations

from typing import Callable

from .evaluation_models import EvaluationCase, EvaluationOutcome


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
