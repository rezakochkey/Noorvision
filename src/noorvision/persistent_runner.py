"""Run Noorvision and persist its history."""

from pathlib import Path

from .agent import NoorvisionAgent
from .history import RunHistory
from .history_runner import run_and_record
from .persistence import load_history, save_history
from .report import RunReport


def run_and_persist(
    agent: NoorvisionAgent,
    count: int,
    path: str | Path,
) -> tuple[RunReport, RunHistory]:
    """Load history, record a real run, persist the updated history, and return both."""
    history_path = Path(path)
    history = load_history(history_path) if history_path.exists() else RunHistory()
    report = run_and_record(agent, count, history)
    save_history(history, history_path)
    return report, history
