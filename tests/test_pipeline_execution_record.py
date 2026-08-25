from noorvision.evaluation_pipeline import run_evaluation
from noorvision.evaluation_task import EvaluationTask


def test_pipeline_executor_receives_original_task_and_output_is_evaluated():
    task = EvaluationTask(
        task_id="math-003",
        input="4 + 4",
        expected_output=8,
    )

    seen = []

    def executor(received_task):
        seen.append(received_task)
        return 8

    outcome = run_evaluation(task, executor)

    assert seen == [task]
    assert outcome.case_id == task.task_id
    assert outcome.passed is True
    assert outcome.score == 1.0
