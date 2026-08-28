from noorvision.evaluation_models import EvaluationOutcome
from noorvision.evaluation_report import build_report


def test_report_retains_outcomes_in_order():
    first = EvaluationOutcome(
        case_id="case-a",
        passed=True,
        score=1.0,
        reason="exact match",
    )
    second = EvaluationOutcome(
        case_id="case-b",
        passed=False,
        score=0.0,
        reason="mismatch",
    )

    report = build_report([first, second])

    assert report.outcomes == (first, second)
    assert report.total == 2
    assert report.passed == 1
    assert report.failed == 1
