"""Run Noorvision cycles and automatically retain their reports."""

from .agent import NoorvisionAgent
from .history import RunHistory
from .report import RunReport
from .report_runner import run_and_report


def run_and_record(
    agent: NoorvisionAgent, count: int, history: RunHistory
) -> RunReport:
    """Run Noorvision, create a report, and append it to history."""
    report = run_and_report(agent, count)
    history.add(report)
    return report
