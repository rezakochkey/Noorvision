from pathlib import Path

from noorvision.history import RunHistory
from noorvision.persistence import load_history, save_history
from noorvision.report import RunReport
from noorvision.runner import RunSummary
from noorvision.snapshot import MemorySnapshot


def make_report(cycles: int) -> RunReport:
    summary = RunSummary(cycles=cycles, experiments=cycles + 1, result_memories=cycles, traces=())
    before = MemorySnapshot(total=cycles, by_kind=(("project", 1),))
    after = MemorySnapshot(total=cycles + 1, by_kind=(("project", 1), ("result", cycles)))
    return RunReport(summary=summary, memory_before=before, memory_after=after)


def test_history_round_trip_preserves_reports(tmp_path: Path) -> None:
    history = RunHistory()
    history.add(make_report(1))
    history.add(make_report(3))
    path = tmp_path / "history.json"

    save_history(history, path)
    restored = load_history(path)

    assert len(restored) == 2
    assert restored.reports == history.reports
    assert restored.latest() == history.latest()
