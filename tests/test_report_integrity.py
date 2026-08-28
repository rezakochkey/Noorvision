from dataclasses import FrozenInstanceError

import pytest

from noorvision.evaluation_batch import run_batch
from noorvision.evaluation_task import EvaluationTask


def test_report_outcomes_are_immutable():
    tasks = [
        EvaluationTask(task_id="math-027-a", input="2 + 2", expected_output=4),
        EvaluationTask(task_id="math-027-b", input="3 + 3", expected_output=6),
    ]

    def executor(task: EvaluationTask) -> int:
        return {"2 + 2": 4, "3 + 3": 6}[task.input]

    report = run_batch(tasks, executor)

    assert report.total == 2
    assert report.passed == 2
    assert report.failed == 0
    assert report.pass_rate == 1.0
    assert len(report.outcomes) == 2

    with pytest.raises((FrozenInstanceError, AttributeError, TypeError)):
        report.outcomes[0] = report.outcomes[1]
