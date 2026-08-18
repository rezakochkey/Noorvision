"""Run bounded Noorvision cycles and summarize their observable behavior."""

from dataclasses import dataclass

from .agent import NoorvisionAgent
from .cycle import run_cycle
from .trace import CycleTrace


@dataclass(frozen=True, slots=True)
class RunSummary:
    cycles: int
    experiments: int
    result_memories: int
    traces: tuple[CycleTrace, ...]


def run_cycles(agent: NoorvisionAgent, count: int) -> RunSummary:
    """Run a finite sequence and return a compact operational summary."""
    if count < 0:
        raise ValueError("count must be non-negative")

    results = tuple(run_cycle(agent) for _ in range(count))
    traces = tuple(result.trace for result in results)

    return RunSummary(
        cycles=len(results),
        experiments=sum(trace.experiment_executed for trace in traces),
        result_memories=sum(trace.result_memory_created for trace in traces),
        traces=traces,
    )
