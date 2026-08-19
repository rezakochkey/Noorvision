from noorvision.analytics import HistoryAnalytics
from noorvision.history import RunHistory
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


def test_history_analytics_aggregates_all_runs() -> None:
    history = RunHistory()
    history.add(make_report(2, 1, 1))
    history.add(make_report(3, 2, 2))
    history.add(make_report(5, 4, 3))

    analytics = HistoryAnalytics.from_history(history)

    assert analytics.total_runs == 3
    assert analytics.total_cycles == 10
    assert analytics.total_experiments == 7
    assert analytics.total_results == 6

    text = analytics.to_text()
    assert "Noorvision History Analytics" in text
    assert "Total Runs: 3" in text
    assert "Total Cycles: 10" in text
