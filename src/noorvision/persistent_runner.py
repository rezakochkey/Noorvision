"""Run Noorvision through the central history service."""

from pathlib import Path

from .agent import NoorvisionAgent
from .history_service import HistoryService
from .history_runner import run_and_record
from .history import RunHistory
from .report import RunReport


def run_and_persist(
    agent: NoorvisionAgent,
    count: int,
    path: str | Path,
) -> tuple[RunReport, RunHistory]:
    """Run Noorvision, record through HistoryService, and return the history."""
    service = HistoryService(path)
    report = run_and_record(agent, count, service.history)
    service.record(report)
    return report, service.history
