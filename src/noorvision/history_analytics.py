"""Convenience analytics for persisted Noorvision history."""

from pathlib import Path

from .analytics import HistoryAnalytics
from .persistence import load_history


def analytics_from_file(path: str | Path) -> HistoryAnalytics:
    """Load persisted history and calculate aggregate analytics."""
    return HistoryAnalytics.from_history(load_history(path))
