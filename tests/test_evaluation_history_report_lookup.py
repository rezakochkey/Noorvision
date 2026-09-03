from noorvision.evaluation_history import EvaluationHistory
from noorvision.evaluation_models import EvaluationOutcome
from noorvision.evaluation_report import EvaluationReport
from noorvision.execution_record import ExecutionRecord


def make_report(execution_id: str) -> EvaluationReport:
    record = ExecutionRecord(
        task_id=f"task-{execution_id}",
        input="2 + 2",
        actual_output=4,
        execution_id=execution_id,
    )
    outcome = EvaluationOutcome(
        case_id=f"case-{execution_id}",
        passed=True,
        score=1.0,
        reason="exact match",
        execution=record,
    )
    return EvaluationReport(
        total=1,
        passed=1,
        failed=0,
        pass_rate=1.0,
        outcomes=(outcome,),
    )


def test_find_report_returns_exact_report_by_execution_id() -> None:
    history = EvaluationHistory()
    first = make_report("exec-033-a")
    second = make_report("exec-033-b")
    history.add(first)
    history.add(second)

    found = history.find_report("exec-033-b")

    assert found is second
    assert found.outcomes[0].execution is not None
    assert found.outcomes[0].execution.execution_id == "exec-033-b"


def test_find_report_returns_none_for_unknown_execution_id() -> None:
    history = EvaluationHistory()
    history.add(make_report("exec-033-a"))

    assert history.find_report("missing-execution") is None
