"""A tiny, observable execution cycle for Noorvision."""

from dataclasses import dataclass

from .agent import AgentStep, NoorvisionAgent


@dataclass(frozen=True, slots=True)
class CycleResult:
    """The observable output of one Noorvision cycle."""

    step: AgentStep


def run_cycle(agent: NoorvisionAgent) -> CycleResult:
    """Observe the current state and return the next proposed action."""
    return CycleResult(step=agent.observe())
