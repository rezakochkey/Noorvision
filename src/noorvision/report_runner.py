"""Build complete reports from real Noorvision runs."""

from .agent import NoorvisionAgent
from .report import RunReport
from .runner import run_cycles
from .snapshot import MemorySnapshot


def run_and_report(agent: NoorvisionAgent, count: int) -> RunReport:
    """Capture memory before and after a bounded run and return its report."""
    before = MemorySnapshot.capture(agent.memory_store)
    summary = run_cycles(agent, count)
    after = MemorySnapshot.capture(agent.memory_store)
    return RunReport(summary=summary, memory_before=before, memory_after=after)
