"""A small, observable execution cycle for Noorvision."""

from dataclasses import dataclass

from .actions import ActionResult, execute_action
from .agent import AgentStep, NoorvisionAgent


@dataclass(frozen=True, slots=True)
class CycleResult:
    """The observable output of one Noorvision cycle."""

    step: AgentStep
    action_result: ActionResult


def run_cycle(agent: NoorvisionAgent) -> CycleResult:
    """Observe, execute the proposed local action, then expose its result."""
    step = agent.observe()
    action_result = execute_action(agent.memory_store, step.decision.action)
    return CycleResult(step=step, action_result=action_result)
