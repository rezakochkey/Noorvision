"""Ordered history of evaluation reports."""

from __future__ import annotations

from dataclasses import dataclass

from .evaluation_report import EvaluationReport


@dataclass(slots=True)
class EvaluationHistory:
    """Ordered in-memory history of completed evaluation reports."""

    reports: list[EvaluationReport]

    def __init__(self) -> None:
        self.reports = []

    def add(self, report: EvaluationReport) -> None:
        """Append a completed report without changing it."""
        self.reports.append(report)

    def latest(self) -> EvaluationReport | None:
        """Return the most recently added report, if any."""
        return self.reports[-1] if self.reports else None

    def __len__(self) -> int:
        return len(self.reports)
