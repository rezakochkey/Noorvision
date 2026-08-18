"""Run a bounded sequence of Noorvision cycles."""

from dataclasses import dataclass

from .agent import NoorvisionAgent
from .cycle import run_cycle


@dataclass(frozen=True, slots=True)
class RunSummary:
    cycles: int
    traces: tuple[object, ...]


def run_cycles(agent: NoorvisionAgent, count: int) -> RunSummary:
    """Run at most the requested finite number of cycles."""
    if count < 0:
        raise ValueError("count must be non-negative")

    results = tuple(run_cycle(agent) for _ in range(count))
    return RunSummary(cycles=len(results), traces=tuple(result.trace for result in results))
