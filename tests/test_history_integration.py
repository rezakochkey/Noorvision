from noorvision.agent import NoorvisionAgent
from noorvision.history import RunHistory
from noorvision.report_runner import run_and_report


def test_run_history_can_store_real_reports() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")
    history = RunHistory()

    first = run_and_report(agent, 1)
    second = run_and_report(agent, 2)
    history.add(first)
    history.add(second)

    assert len(history) == 2
    assert history.latest() is second
    assert history.reports[0].summary.cycles == 1
    assert history.reports[1].summary.cycles == 2
