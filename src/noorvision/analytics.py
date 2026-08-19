"""Aggregate analytics over Noorvision run history."""

from dataclasses import dataclass

from .history import RunHistory


@dataclass(frozen=True, slots=True)
class HistoryAnalytics:
    total_runs: int
    total_cycles: int
    total_experiments: int
    total_results: int

    @classmethod
    def from_history(cls, history: RunHistory) -> "HistoryAnalytics":
        return cls(
            total_runs=len(history),
            total_cycles=sum(r.summary.cycles for r in history.reports),
            total_experiments=sum(r.summary.experiments for r in history.reports),
            total_results=sum(r.summary.result_memories for r in history.reports),
        )

    def to_text(self) -> str:
        return "\n".join(
            (
                "Noorvision History Analytics",
                f"Total Runs: {self.total_runs}",
                f"Total Cycles: {self.total_cycles}",
                f"Total Experiments: {self.total_experiments}",
                f"Total Results: {self.total_results}",
            )
        )
