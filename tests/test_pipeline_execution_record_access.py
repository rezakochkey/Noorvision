from noorvision.evaluation_pipeline import run_evaluation
from noorvision.evaluation_task import EvaluationTask


def test_pipeline_result_exposes_execution_record():
    task = EvaluationTask(
        task_id="math-025",
        input="5 + 5",
        expected_output=10,
    )

    result = run_evaluation(task, lambda received: 10)

    assert result.execution.task_id == task.task_id
    assert result.execution.input == task.input
    assert result.execution.actual_output == 10
