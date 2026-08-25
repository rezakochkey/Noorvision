from noorvision.evaluation_batch import run_batch
from noorvision.evaluation_task import EvaluationTask


def test_batch_runs_multiple_tasks_and_aggregates_report():
    tasks = [
        EvaluationTask(task_id="math-001", input="2 + 2", expected_output=4),
        EvaluationTask(task_id="math-002", input="3 + 3", expected_output=6),
        EvaluationTask(task_id="math-003", input="4 + 4", expected_output=8),
    ]

    answers = {"2 + 2": 4, "3 + 3": 6, "4 + 4": 5}

    report = run_batch(tasks, lambda task: answers[task.input])

    assert report.total == 3
    assert report.passed == 2
    assert report.failed == 1
    assert report.pass_rate == 2 / 3


def test_empty_batch_produces_empty_report():
    report = run_batch([], lambda task: task.input)

    assert report.total == 0
    assert report.passed == 0
    assert report.failed == 0
    assert report.pass_rate == 0.0
