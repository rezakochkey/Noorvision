"""Run Noorvision through the central history service."""

from pathlib import Path

from .agent import NoorvisionAgent
from .history_service import HistoryService
from .report import RunReport
from .report_runner import run_and_report


def run_and_persist(
    agent: NoorvisionAgent,
    count: int,
    path: str | Path,
) -> tuple[RunReport, HistoryService]:
    """Run Noorvision, record the report through HistoryService, and persist it."""
    service = HistoryService(path)
    report = run_and_report(agent, count)
    service.record(report)
    return report, service.history
