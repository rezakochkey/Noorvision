"""JSON persistence for Noorvision run history."""

from dataclasses import asdict
import json
from pathlib import Path

from .history import RunHistory
from .report import RunReport
from .runner import RunSummary
from .snapshot import MemorySnapshot


def save_history(history: RunHistory, path: str | Path) -> None:
    """Persist run history as readable JSON."""
    payload = [asdict(report) for report in history.reports]
    Path(path).write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")


def load_history(path: str | Path) -> RunHistory:
    """Load run history persisted by :func:`save_history`."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    history = RunHistory()
    for item in raw:
        summary_data = item["summary"]
        summary = RunSummary(**summary_data)
        before = MemorySnapshot(**item["memory_before"])
        after = MemorySnapshot(**item["memory_after"])
        history.add(RunReport(summary=summary, memory_before=before, memory_after=after))
    return history
