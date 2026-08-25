import pytest

from noorvision.execution_record import ExecutionRecord


def test_execution_record_preserves_execution_data():
    record = ExecutionRecord(
        task_id="math-001",
        input="2 + 2",
        actual_output=4,
    )

    assert record.task_id == "math-001"
    assert record.input == "2 + 2"
    assert record.actual_output == 4


def test_execution_record_rejects_empty_task_id():
    with pytest.raises(ValueError, match="task_id must not be empty"):
        ExecutionRecord(task_id="", input="2 + 2", actual_output=4)


def test_execution_record_is_immutable():
    record = ExecutionRecord(
        task_id="math-001",
        input="2 + 2",
        actual_output=4,
    )

    with pytest.raises(AttributeError):
        record.actual_output = 5
