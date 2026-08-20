"""Queries over Noorvision run history."""

from .history import RunHistory
from .report import RunReport


def latest_reports(history: RunHistory, limit: int = 5) -> list[RunReport]:
    """Return up to ``limit`` reports, newest first."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    return list(reversed(history.reports[-limit:])) if limit else []


def reports_with_experiments(history: RunHistory) -> list[RunReport]:
    """Return reports that recorded at least one experiment."""
    return [report for report in history.reports if report.summary.experiments > 0]


def highest_cycle_run(history: RunHistory) -> RunReport | None:
    """Return the report with the highest cycle count, if history is non-empty."""
    return max(history.reports, key=lambda report: report.summary.cycles, default=None)
