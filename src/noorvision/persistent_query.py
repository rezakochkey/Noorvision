"""Queries over persisted Noorvision run history."""

from pathlib import Path

from .history import RunHistory
from .persistence import load_history
from .query import highest_cycle_run, latest_reports, reports_with_experiments
from .report import RunReport


def _load(path: str | Path) -> RunHistory:
    return load_history(path)


def latest_reports_from_file(path: str | Path, limit: int = 5) -> list[RunReport]:
    return latest_reports(_load(path), limit)


def reports_with_experiments_from_file(path: str | Path) -> list[RunReport]:
    return reports_with_experiments(_load(path))


def highest_cycle_run_from_file(path: str | Path) -> RunReport | None:
    return highest_cycle_run(_load(path))
