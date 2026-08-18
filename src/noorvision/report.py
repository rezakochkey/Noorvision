"""Human-readable reports for Noorvision runs."""

from dataclasses import dataclass

from .runner import RunSummary
from .snapshot import MemorySnapshot


@dataclass(frozen=True, slots=True)
class RunReport:
    """A compact report combining execution and memory state."""

    summary: RunSummary
    memory_before: MemorySnapshot
    memory_after: MemorySnapshot

    @property
    def status(self) -> str:
        return "SUCCESS"

    def to_text(self) -> str:
        return "\n".join(
            (
                "Noorvision Run Report",
                f"Cycles: {self.summary.cycles}",
                f"Experiments: {self.summary.experiments}",
                f"Results: {self.summary.result_memories}",
                f"Memory Before: {self.memory_before.total}",
                f"Memory After: {self.memory_after.total}",
                f"Status: {self.status}",
            )
        )
