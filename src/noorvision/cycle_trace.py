"""Build a trace without changing the existing cycle contract yet."""

from .actions import ActionResult
from .agent import AgentStep
from .trace import CycleTrace


def trace_cycle(
    step: AgentStep,
    action_result: ActionResult,
    *,
    experiment_executed: bool = False,
    result_memory_created: bool = False,
) -> CycleTrace:
    """Create an inspectable trace from an observed cycle step."""
    return CycleTrace.from_step(
        step,
        action_result,
        experiment_executed=experiment_executed,
        result_memory_created=result_memory_created,
    )
