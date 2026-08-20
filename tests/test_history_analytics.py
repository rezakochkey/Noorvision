from pathlib import Path

from noorvision.history_analytics import analytics_from_file
from noorvision.history import RunHistory
from noorvision.persistence import save_history
from noorvision.report import RunReport
from noorvision.runner import RunSummary
from noorvision.snapshot import MemorySnapshot


def make_report(cycles: int, experiments: int, results: int) -> RunReport:
    summary = RunSummary(
        cycles=cycles,
        experiments=experiments,
        result_memories=results,
        traces=(),
    )
    snapshot = MemorySnapshot(total=0, by_kind=())
    return RunReport(summary=summary, memory_before=snapshot, memory_after=snapshot)


def test_analytics_from_file_reads_persisted_history(tmp_path: Path) -> None:
    history = RunHistory()
    history.add(make_report(2, 1, 1))
    history.add(make_report(3, 2, 2))
    path = tmp_path / "history.json"
    save_history(history, path)

    analytics = analytics_from_file(path)

    assert analytics.total_runs == 2
    assert analytics.total_cycles == 5
    assert analytics.total_experiments == 3
    assert analytics.total_results == 3
