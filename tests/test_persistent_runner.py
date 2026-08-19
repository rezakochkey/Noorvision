from pathlib import Path

from noorvision.agent import NoorvisionAgent
from noorvision.persistence import load_history
from noorvision.persistent_runner import run_and_persist


def test_run_and_persist_accumulates_history_across_runs(tmp_path: Path) -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")
    path = tmp_path / "history.json"

    first_report, first_history = run_and_persist(agent, 1, path)
    assert len(first_history) == 1
    assert first_history.latest() == first_report

    second_report, second_history = run_and_persist(agent, 2, path)
    assert len(second_history) == 2
    assert second_history.latest() == second_report

    restored = load_history(path)
    assert len(restored) == 2
    assert restored.reports[0] == first_report
    assert restored.reports[1] == second_report
