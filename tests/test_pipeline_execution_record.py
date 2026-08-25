from noorvision.evaluation_pipeline import run_evaluation
from noorvision.evaluation_task import EvaluationTask


def test_pipeline_executor_receives_task_and_produces_evaluated_output():
    task = EvaluationTask(
        task_id="math-004",
        input="2 + 2",
        expected_output=4,
    )

    received = []

    def executor(received_task):
        received.append(received_task)
        return 4

    outcome = run_evaluation(task, executor)

    assert received == [task]
    assert outcome.case_id == task.task_id
    assert outcome.passed is True
    assert outcome.score == 1.0
