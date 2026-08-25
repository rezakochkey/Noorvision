"""End-to-end deterministic pipeline from task to evaluation outcome."""

from __future__ import annotations

from typing import Any, Callable

from .evaluation_bridge import case_from_task
from .evaluation_models import EvaluationOutcome
from .evaluation_task import EvaluationTask
from .evaluator import evaluate_case


Executor = Callable[[EvaluationTask], Any]


def run_evaluation(task: EvaluationTask, executor: Executor) -> EvaluationOutcome:
    """Execute a task, build its case, and evaluate the observed output."""
    actual_output = executor(task)
    case = case_from_task(task, actual_output)
    return evaluate_case(case)
