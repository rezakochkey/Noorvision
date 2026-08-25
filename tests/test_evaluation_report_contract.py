from dataclasses import dataclass

from noorvision.evaluation import EvaluationResult


@dataclass(frozen=True)
class EvaluationReport:
    results: tuple[EvaluationResult, ...]

    @property
    def total(self) -> int:
        return len(self.results)

    @property
    def passed(self) -> int:
        return sum(result.status == "pass" for result in self.results)

    @property
    def failed(self) -> int:
        return sum(result.status == "fail" for result in self.results)

    @property
    def pass_rate(self) -> float:
        return self.passed / self.total if self.total else 0.0


def test_report_counts_and_pass_rate() -> None:
    results = (
        EvaluationResult(case_id="case-1", status="pass", score=1.0, reason="exact match"),
        EvaluationResult(case_id="case-2", status="fail", score=0.0, reason="mismatch"),
    )

    report = EvaluationReport(results=results)

    assert report.total == 2
    assert report.passed == 1
    assert report.failed == 1
    assert report.pass_rate == 0.5


def test_empty_report_has_zero_pass_rate() -> None:
    report = EvaluationReport(results=())

    assert report.total == 0
    assert report.passed == 0
    assert report.failed == 0
    assert report.pass_rate == 0.0
