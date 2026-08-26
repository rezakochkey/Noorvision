from noorvision.evaluation_batch import run_batch
from noorvision.evaluation_task import EvaluationTask


def test_batch_preserves_distinct_execution_records():
    tasks = [
        EvaluationTask(task_id="math-026-a", input="2 + 2", expected_output=4),
        EvaluationTask(task_id="math-026-b", input="3 + 3", expected_output=6),
        EvaluationTask(task_id="math-026-c", input="4 + 4", expected_output=8),
    ]

    answers = {"2 + 2": 4, "3 + 3": 6, "4 + 4": 8}
    report = run_batch(tasks, lambda value: answers[value])

    assert report.total == 3
    assert report.passed == 3

    records = [outcome.execution for outcome in report.outcomes]

    assert all(record is not None for record in records)
    assert [record.task_id for record in records] == [task.task_id for task in tasks]
    assert [record.input for record in records] == [task.input for task in tasks]
    assert [record.actual_output for record in records] == [4, 6, 8]
    assert len({id(record) for record in records}) == 3
