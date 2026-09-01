from noorvision.execution_record import ExecutionRecord


def test_execution_records_have_distinct_immutable_identities():
    first = ExecutionRecord(task_id="task-a", input="alpha", actual_output="A")
    second = ExecutionRecord(task_id="task-b", input="beta", actual_output="B")

    assert first.execution_id
    assert second.execution_id
    assert first.execution_id != second.execution_id

    try:
        first.execution_id = "replacement"
    except (AttributeError, TypeError):
        pass
    else:
        raise AssertionError("execution_id must be immutable")
