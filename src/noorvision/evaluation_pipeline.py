"""End-to-end deterministic pipeline from task to evaluation outcome."""

from __future__ import annotations

from dataclasses import replace
from typing import Any, Callable

from .evaluation_bridge import case_from_task
from .evaluation_models import EvaluationOutcome
from .evaluation_task import EvaluationTask
from .evaluator import evaluate_case
from .execution_record import ExecutionRecord


Executor = Callable[[EvaluationTask], Any]


def run_evaluation(task: EvaluationTask, executor: Executor) -> EvaluationOutcome:
    """Execute a task, record its observable output, and evaluate it."""
    record = ExecutionRecord(
        task_id=task.task_id,
        input=task.input,
        actual_output=executor(task),
    )
    case = case_from_task(task, record.actual_output)
    outcome = evaluate_case(case)
    return replace(outcome, execution=record)
