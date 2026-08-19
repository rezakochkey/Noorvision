from noorvision.agent import NoorvisionAgent
from noorvision.report_runner import run_and_report


def test_run_and_report_connects_real_run_to_report() -> None:
    agent = NoorvisionAgent()
    agent.capture_context("Noorvision", "Initial project context")

    report = run_and_report(agent, 2)

    assert report.summary.cycles == 2
    assert len(report.summary.traces) == 2
    assert report.memory_after.total >= report.memory_before.total
    text = report.to_text()
    assert "Noorvision Run Report" in text
    assert "Cycles: 2" in text
    assert "Status: SUCCESS" in text
