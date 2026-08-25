from noorvision.history import RunHistory
from noorvision.persistence import load_history, save_history
from noorvision.query import highest_cycle_run, latest_reports, reports_with_experiments
from noorvision.report import RunReport
from noorvision.runner import RunSummary
from noorvision.snapshot import MemorySnapshot
from noorvision.trace import CycleTrace


def _report(*, cycle: int, experiment: bool) -> RunReport:
    trace = CycleTrace(
        action="run_next_experiment" if experiment else "record_decision",
        memory_count_before=cycle - 1,
        action_memory_created=True,
        experiment_executed=experiment,
        result_memory_created=experiment,
    )
    summary = RunSummary(
        cycles=cycle,
        experiments=int(experiment),
        result_memories=int(experiment),
        traces=(trace,),
    )
    snapshot = MemorySnapshot(total=cycle, by_kind=())
    return RunReport(summary=summary, memory_before=snapshot, memory_after=snapshot)


def test_persistence_round_trip_preserves_query_contract(tmp_path) -> None:
    path = tmp_path / "history.json"
    history = RunHistory()
    first = _report(cycle=1, experiment=True)
    second = _report(cycle=2, experiment=False)
    history.add(first)
    history.add(second)

    save_history(history, path)
    loaded = load_history(path)

    assert len(loaded) == 2
    assert loaded.latest() is not None
    assert latest_reports(loaded, 2) == [second, first]
    assert reports_with_experiments(loaded) == [first]
    assert highest_cycle_run(loaded) == second

    save_history(loaded, path)
    reloaded = load_history(path)
    assert latest_reports(reloaded, 2) == [second, first]


def test_query_empty_and_boundary_contracts() -> None:
    history = RunHistory()

    assert latest_reports(history, 0) == []
    assert reports_with_experiments(history) == []
    assert highest_cycle_run(history) is None

    try:
        latest_reports(history, -1)
    except ValueError as exc:
        assert str(exc) == "limit must be non-negative"
    else:
        raise AssertionError("negative query limit must be rejected")
