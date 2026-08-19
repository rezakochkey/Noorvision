"""In-memory history of Noorvision run reports."""

from dataclasses import dataclass

from .report import RunReport


@dataclass(slots=True)
class RunHistory:
    """Ordered, bounded history of completed reports."""

    reports: list[RunReport]

    def __init__(self) -> None:
        self.reports = []

    def add(self, report: RunReport) -> None:
        self.reports.append(report)

    def latest(self) -> RunReport | None:
        return self.reports[-1] if self.reports else None

    def __len__(self) -> int:
        return len(self.reports)
