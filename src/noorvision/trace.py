"""Observable execution traces for Noorvision cycles."""

from dataclasses import dataclass

from .actions import ActionResult
from .agent import AgentStep


@dataclass(frozen=True, slots=True)
class CycleTrace:
    """A compact, inspectable record of one cycle."""

    action: str
    memory_count_before: int
    action_memory_created: bool
    experiment_executed: bool
    result_memory_created: bool

    @classmethod
    def from_step(
        cls,
        step: AgentStep,
        action_result: ActionResult,
        *,
        experiment_executed: bool = False,
        result_memory_created: bool = False,
    ) -> "CycleTrace":
        return cls(
            action=step.decision.action,
            memory_count_before=step.memory_count,
            action_memory_created=action_result.memory is not None,
            experiment_executed=experiment_executed,
            result_memory_created=result_memory_created,
        )
