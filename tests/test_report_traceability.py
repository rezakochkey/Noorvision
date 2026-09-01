from noorvision.evaluation_batch import run_batch
from noorvision.evaluation_task import EvaluationTask


def test_report_outcomes_remain_traceable_to_their_execution_records():
    tasks = [
        EvaluationTask(task_id="trace-028-a", input="alpha", expected_output="A"),
        EvaluationTask(task_id="trace-028-b", input="beta", expected_output="B"),
    ]

    def executor(task: EvaluationTask) -> str:
        return {"alpha": "A", "beta": "B"}[task.input]

    report = run_batch(tasks, executor)

    assert report.total == 2
    assert len(report.outcomes) == 2

    for task, outcome in zip(tasks, report.outcomes):
        assert outcome.execution is not None
        assert outcome.execution.task_id == task.task_id
        assert outcome.execution.input == task.input
        assert outcome.execution.actual_output == task.expected_output
