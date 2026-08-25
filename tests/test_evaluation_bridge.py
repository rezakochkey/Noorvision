from noorvision.evaluation_bridge import case_from_task
from noorvision.evaluation_task import EvaluationTask


def test_case_from_task_preserves_expected_and_actual():
    task = EvaluationTask(
        task_id="addition-001",
        input="2 + 2",
        expected_output=4,
    )

    case = case_from_task(task, 4)

    assert case.case_id == "addition-001"
    assert case.expected == 4
    assert case.actual == 4


def test_case_from_task_preserves_failure_output():
    task = EvaluationTask(
        task_id="addition-002",
        input="2 + 2",
        expected_output=4,
    )

    case = case_from_task(task, 5)

    assert case.expected == 4
    assert case.actual == 5
