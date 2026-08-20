from pathlib import Path

from noorvision.history import RunHistory
from noorvision.persistence import save_history
from noorvision.persistent_query import (
    highest_cycle_run_from_file,
    latest_reports_from_file,
    reports_with_experiments_from_file,
)
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


def test_persistent_queries_match_saved_history(tmp_path: Path) -> None:
    history = RunHistory()
    first = make_report(2, 0)
    second = make_report(5, 2)
    third = make_report(3, 1)
    history.add(first)
    history.add(second)
    history.add(third)

    path = tmp_path / "history.json"
    save_history(history, path)

    assert latest_reports_from_file(path, 2) == [third, second]
    assert reports_with_experiments_from_file(path) == [second, third]
    assert highest_cycle_run_from_file(path) == second
