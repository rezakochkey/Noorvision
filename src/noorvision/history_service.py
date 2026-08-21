"""Central service for Noorvision history, persistence, queries, and analytics."""

from pathlib import Path

from .agent import NoorvisionAgent
from .analytics import HistoryAnalytics
from .history import RunHistory
from .persistence import load_history, save_history
from .query import highest_cycle_run, latest_reports, reports_with_experiments
from .report import RunReport
from .report_runner import run_and_report


class HistoryService:
    """Coordinate history loading, execution, saving, querying, and analytics."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.history = load_history(self.path) if self.path.exists() else RunHistory()

    def run(self, agent: NoorvisionAgent, count: int) -> RunReport:
        """Run Noorvision, record the report once, and persist the updated history."""
        report = run_and_report(agent, count)
        self.record(report)
        return report

    def record(self, report: RunReport) -> None:
        self.history.add(report)
        save_history(self.history, self.path)

    def latest(self, limit: int = 5) -> list[RunReport]:
        return latest_reports(self.history, limit)

    def with_experiments(self) -> list[RunReport]:
        return reports_with_experiments(self.history)

    def highest_cycle(self) -> RunReport | None:
        return highest_cycle_run(self.history)

    def analytics(self) -> HistoryAnalytics:
        return HistoryAnalytics.from_history(self.history)
