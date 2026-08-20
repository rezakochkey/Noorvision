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


def test_history_service_coordinates_persistence_queries_and_analytics(tmp_path: Path) -> None:
    path = tmp_path / "history.json"
    service = HistoryService(path)
    first = make_report(2, 1)
    second = make_report(5, 2)

    service.record(first)
    service.record(second)

    restored = HistoryService(path)
    assert len(restored.history) == 2
    assert restored.latest(1) == [second]
    assert restored.with_experiments() == [first, second]
    assert restored.highest_cycle() == second
    assert restored.analytics().total_runs == 2
    assert restored.analytics().total_cycles == 7
