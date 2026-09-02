"""Ordered history of evaluation reports."""

from __future__ import annotations

from dataclasses import dataclass

from .evaluation_models import EvaluationOutcome
from .evaluation_report import EvaluationReport
from .execution_record import ExecutionRecord


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

    def find_execution(self, execution_id: str) -> ExecutionRecord | None:
        """Return the execution record with the given id, if present."""
        for report in self.reports:
            for outcome in report.outcomes:
                execution = outcome.execution
                if execution is not None and execution.execution_id == execution_id:
                    return execution
        return None

    def find_outcome(self, execution_id: str) -> EvaluationOutcome | None:
        """Return the evaluation outcome linked to an execution id, if present."""
        for report in self.reports:
            for outcome in report.outcomes:
                execution = outcome.execution
                if execution is not None and execution.execution_id == execution_id:
                    return outcome
        return None

    def __len__(self) -> int:
        return len(self.reports)
