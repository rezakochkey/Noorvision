"""Run multiple evaluation tasks and aggregate their outcomes."""

from __future__ import annotations

from collections.abc import Callable, Iterable

from .evaluation_models import EvaluationOutcome
from .evaluation_pipeline import run_evaluation
from .evaluation_report import EvaluationReport, build_report
from .evaluation_task import EvaluationTask


def run_batch(
    tasks: Iterable[EvaluationTask],
    executor: Callable[[object], object],
) -> EvaluationReport:
    """Evaluate all tasks in order and aggregate their outcomes."""
    outcomes: list[EvaluationOutcome] = [
        run_evaluation(task, executor) for task in tasks
    ]
    return build_report(outcomes)
