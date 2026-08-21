"""Compatibility wrapper for running Noorvision with persisted history."""

from pathlib import Path

from .agent import NoorvisionAgent
from .history_service import HistoryService
from .report import RunReport


def run_and_persist(
    agent: NoorvisionAgent,
    count: int,
    path: str | Path,
) -> tuple[RunReport, object]:
    """Run through HistoryService while preserving the legacy return contract."""
    service = HistoryService(path)
    report = service.run(agent, count)
    return report, service.history
