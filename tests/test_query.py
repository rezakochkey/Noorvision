from noorvision.history import RunHistory
from noorvision.query import highest_cycle_run, latest_reports, reports_with_experiments
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


def test_history_queries_return_expected_reports() -> None:
    history = RunHistory()
    first = make_report(2, 0)
    second = make_report(5, 2)
    third = make_report(3, 1)
    history.add(first)
    history.add(second)
    history.add(third)

    assert latest_reports(history, 2) == [third, second]
    assert reports_with_experiments(history) == [second, third]
    assert highest_cycle_run(history) is second


def test_latest_reports_rejects_negative_limit() -> None:
    history = RunHistory()
    try:
        latest_reports(history, -1)
    except ValueError as exc:
        assert str(exc) == "limit must be non-negative"
    else:
        raise AssertionError("negative limit should raise ValueError")
