import pytest

from noorvision.evaluation_task import EvaluationTask


def test_evaluation_task_preserves_input_and_expected_output():
    task = EvaluationTask(
        task_id="task-001",
        input="What is 2 + 2?",
        expected_output="4",
    )

    assert task.task_id == "task-001"
    assert task.input == "What is 2 + 2?"
    assert task.expected_output == "4"


def test_evaluation_task_rejects_empty_task_id():
    with pytest.raises(ValueError, match="task_id must not be empty"):
        EvaluationTask(task_id="", input="2 + 2", expected_output="4")
