from noorvision.agent import NoorvisionAgent
from noorvision.cycle import run_cycle
from noorvision.history import RunHistory
from noorvision.history_service import HistoryService
from noorvision.persistence import load_history, save_history
from noorvision.query import highest_cycle_run, latest_reports, reports_with_experiments


def test_persistence_round_trip_preserves_query_contract(tmp_path) -> None:
    path = tmp_path / "history.json"
    service = HistoryService(path)
    agent = NoorvisionAgent()

    first = service.run(agent, 1)

    experiment_agent = NoorvisionAgent()
    experiment_agent.capture_context("Noorvision", "Experiment context")
    experiment_result = run_cycle(experiment_agent)
    assert experiment_result.trace.experiment_executed is True
    second = service.run(agent, 2)
    service.history.records[-1] = second

    loaded = load_history(path)

    assert len(loaded) == 2
    assert loaded.latest() is not None
    assert latest_reports(loaded, 2) == [second, first]
    assert reports_with_experiments(loaded) == [first]
    assert highest_cycle_run(loaded) is second

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
