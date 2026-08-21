from pathlib import Path

from noorvision.history_service import HistoryService
from noorvision.report import RunReport


class FakeAgent:
    """Minimal agent shape for verifying service orchestration."""

    def run(self, count: int):
        raise AssertionError("service should delegate through report_runner")


def test_history_service_run_records_exactly_once(tmp_path: Path, monkeypatch) -> None:
    from noorvision import history_service

    report = object()
    calls = []

    def fake_run_and_report(agent, count):
        calls.append((agent, count))
        return report

    monkeypatch.setattr(history_service, "run_and_report", fake_run_and_report)

    service = HistoryService(tmp_path / "history.json")
    result = service.run(FakeAgent(), 3)

    assert result is report
    assert calls[0][1] == 3
    assert len(service.history) == 1
    assert service.history.latest() is report
    assert (tmp_path / "history.json").exists()
