from pathlib import Path

from noorvision.history_service import HistoryService
from noorvision.report import RunReport
from noorvision.runner import RunSummary
from noorvision.snapshot import MemorySnapshot


def make_report(cycles: int, experiments: int) -> RunReport:
    summary = RunSummary(
        cycles=cycles,
        experiments=experiments,
        result_memories=experiments,
        traces=(),
    )
    snapshot = MemorySnapshot(total=0, by_kind=())
    return RunReport(summary=summary, memory_before=snapshot, memory_after=snapshot)


def test_record_is_durable_and_idempotent_for_the_same_report(tmp_path: Path) -> None:
    path = tmp_path / "history.json"
    service = HistoryService(path)
    report = make_report(4, 2)

    service.record(report)
    first_count = len(service.history)
    service.record(report)

    assert first_count == 1
    assert len(service.history) == 2

    restored = HistoryService(path)
    assert len(restored.history) == 2
    assert restored.latest(2) == [report, report]


def test_empty_service_provides_safe_query_and_analytics_defaults(tmp_path: Path) -> None:
    service = HistoryService(tmp_path / "missing.json")

    assert service.latest() == []
    assert service.with_experiments() == []
    assert service.highest_cycle() is None
    assert service.analytics().total_runs == 0
    assert service.analytics().total_cycles == 0
