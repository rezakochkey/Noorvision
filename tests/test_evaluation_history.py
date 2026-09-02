from noorvision.evaluation_history import EvaluationHistory
from noorvision.evaluation_models import EvaluationOutcome
from noorvision.evaluation_report import EvaluationReport
from noorvision.execution_record import ExecutionRecord


def make_report() -> EvaluationReport:
    record = ExecutionRecord(
        task_id="math-030",
        input="2 + 2",
        actual_output=4,
        execution_id="exec-030",
    )
    outcome = EvaluationOutcome(
        case_id="math-030",
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


def test_evaluation_history_preserves_report_and_execution_trace() -> None:
    history = EvaluationHistory()
    report = make_report()

    assert history.latest() is None

    history.add(report)

    assert len(history) == 1
    assert history.latest() is report
    assert history.reports == [report]
    assert history.latest().outcomes[0].execution is report.outcomes[0].execution
    assert history.latest().outcomes[0].execution.execution_id == "exec-030"
