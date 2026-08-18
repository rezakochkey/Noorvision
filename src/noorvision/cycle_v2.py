"""Cycle execution with an observable trace."""

from dataclasses import dataclass

from .actions import ActionResult, execute_action
from .agent import AgentStep, NoorvisionAgent
from .experiment import Experiment
from .experiment_runner import run_experiment
from .learning import remember_result
from .trace import CycleTrace


@dataclass(frozen=True, slots=True)
class CycleResult:
    """The observable output of one Noorvision cycle."""

    step: AgentStep
    action_result: ActionResult
    trace: CycleTrace


def run_cycle(agent: NoorvisionAgent) -> CycleResult:
    """Observe, execute, learn, and expose an inspectable trace."""
    step = agent.observe()
    action_result = execute_action(agent.memory_store, step.decision.action)
    experiment_executed = False
    result_memory_created = False

    if step.decision.action == "run_next_experiment":
        experiment = Experiment(
            hypothesis="Validate the next explicit Noorvision hypothesis.",
            success_criteria="A local experiment result is produced and stored as memory.",
        )
        result = run_experiment(experiment)
        memory = remember_result(experiment, result)
        agent.memory_store.add(memory)
        experiment_executed = True
        result_memory_created = True

    trace = CycleTrace.from_step(
        step,
        action_result,
        experiment_executed=experiment_executed,
        result_memory_created=result_memory_created,
    )
    return CycleResult(step=step, action_result=action_result, trace=trace)
