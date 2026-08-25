from dataclasses import dataclass


@dataclass(frozen=True)
class Outcome:
    passed: bool
    score: float


def build_report(outcomes: list[Outcome]) -> dict[str, float | int]:
    total = len(outcomes)
    passed = sum(outcome.passed for outcome in outcomes)
    failed = total - passed
    pass_rate = passed / total if total else 0.0
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": pass_rate,
    }


def test_report_aggregates_pass_and_fail_outcomes():
    report = build_report([Outcome(True, 1.0), Outcome(False, 0.0)])
    assert report == {
        "total": 2,
        "passed": 1,
        "failed": 1,
        "pass_rate": 0.5,
    }


def test_empty_report_has_zero_pass_rate():
    assert build_report([]) == {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "pass_rate": 0.0,
    }


def test_report_does_not_use_score_to_reclassify_failures():
    report = build_report([Outcome(False, 1.0)])
    assert report["failed"] == 1
    assert report["passed"] == 0
