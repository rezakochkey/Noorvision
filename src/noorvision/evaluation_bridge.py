"""Bridge task definitions to executable evaluation cases."""

from __future__ import annotations

from typing import Any

from .evaluation_models import EvaluationCase
from .evaluation_task import EvaluationTask


def case_from_task(task: EvaluationTask, actual_output: Any) -> EvaluationCase:
    """Create an evaluation case from a task and its observed output."""
    return EvaluationCase(
        case_id=task.task_id,
        expected=task.expected_output,
        actual=actual_output,
    )
