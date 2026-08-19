"""JSON persistence for Noorvision run history."""

from dataclasses import asdict
import json
from pathlib import Path

from .history import RunHistory
from .report import RunReport
from .runner import RunSummary
from .snapshot import MemorySnapshot
from .trace import CycleTrace


def save_history(history: RunHistory, path: str | Path) -> None:
    """Persist run history as readable JSON."""
    payload = [asdict(report) for report in history.reports]
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_history(path: str | Path) -> RunHistory:
    """Load run history persisted by :func:`save_history`."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    history = RunHistory()
    for item in raw:
        summary_data = item["summary"]
        traces = tuple(CycleTrace(**trace) for trace in summary_data["traces"])
        summary = RunSummary(
            cycles=summary_data["cycles"],
            experiments=summary_data["experiments"],
            result_memories=summary_data["result_memories"],
            traces=traces,
        )
        before_data = item["memory_before"]
        after_data = item["memory_after"]
        before = MemorySnapshot(
            total=before_data["total"],
            by_kind=tuple(tuple(entry) for entry in before_data["by_kind"]),
        )
        after = MemorySnapshot(
            total=after_data["total"],
            by_kind=tuple(tuple(entry) for entry in after_data["by_kind"]),
        )
        history.add(RunReport(summary=summary, memory_before=before, memory_after=after))
    return history
