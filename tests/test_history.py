from noorvision.history import RunHistory
from noorvision.report import RunReport
from noorvision.runner import RunSummary
from noorvision.snapshot import MemorySnapshot


def make_report(cycles: int) -> RunReport:
    summary = RunSummary(cycles=cycles, experiments=0, result_memories=0, traces=())
    snapshot = MemorySnapshot(total=cycles, by_kind=())
    return RunReport(summary=summary, memory_before=snapshot, memory_after=snapshot)


def test_run_history_preserves_order_and_latest_report() -> None:
    history = RunHistory()
    first = make_report(1)
    second = make_report(2)

    assert history.latest() is None

    history.add(first)
    history.add(second)

    assert len(history) == 2
    assert history.reports == [first, second]
    assert history.latest() is second
