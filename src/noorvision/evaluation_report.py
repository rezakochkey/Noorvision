"""Aggregation of evaluation outcomes into a deterministic report."""

from __future__ import annotations

from dataclasses import dataclass

from .evaluation_models import EvaluationOutcome


@dataclass(frozen=True, slots=True)
class EvaluationReport:
    """Aggregate results from one evaluation run."""

    total: int
    passed: int
    failed: int
    pass_rate: float


def build_report(outcomes: list[EvaluationOutcome]) -> EvaluationReport:
    """Build a report without allowing score to redefine pass/fail status."""
    total = len(outcomes)
    passed = sum(outcome.passed for outcome in outcomes)
    failed = total - passed
    pass_rate = passed / total if total else 0.0
    return EvaluationReport(
        total=total,
        passed=passed,
        failed=failed,
        pass_rate=pass_rate,
    )
