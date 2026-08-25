from noorvision.evaluation_pipeline import run_evaluation
from noorvision.evaluation_task import EvaluationTask


def test_pipeline_runs_task_to_passing_outcome():
    task = EvaluationTask(
        task_id="math-001",
        input="2 + 2",
        expected_output=4,
    )

    outcome = run_evaluation(task, lambda value: 4)

    assert outcome.case_id == "math-001"
    assert outcome.passed is True
    assert outcome.score == 1.0
    assert outcome.reason == "exact match"


def test_pipeline_preserves_wrong_executor_output_as_failure():
    task = EvaluationTask(
        task_id="math-002",
        input="2 + 2",
        expected_output=4,
    )

    outcome = run_evaluation(task, lambda value: 5)

    assert outcome.case_id == "math-002"
    assert outcome.passed is False
    assert outcome.score == 0.0
    assert outcome.reason == "actual value does not match expected value"
