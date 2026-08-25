from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationTask:
    case_id: str
    input: object
    expected_output: object


@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    expected: object
    actual: object


def execute_task(task: EvaluationTask, actual_output: object) -> EvaluationCase:
    return EvaluationCase(
        case_id=task.case_id,
        expected=task.expected_output,
        actual=actual_output,
    )


def test_task_execution_creates_case_without_changing_expected_output():
    task = EvaluationTask(case_id="addition-001", input="2+2", expected_output=4)

    case = execute_task(task, 4)

    assert case == EvaluationCase(case_id="addition-001", expected=4, actual=4)


def test_task_execution_preserves_failure_as_actual_output():
    task = EvaluationTask(case_id="addition-002", input="2+2", expected_output=4)

    case = execute_task(task, 5)

    assert case == EvaluationCase(case_id="addition-002", expected=4, actual=5)
