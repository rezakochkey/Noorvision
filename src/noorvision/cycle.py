"""A small, observable execution cycle for Noorvision."""

from dataclasses import dataclass

from .actions import ActionResult, execute_action
from .agent import AgentStep, NoorvisionAgent
from .experiment import Experiment
from .experiment_runner import run_experiment
from .learning import remember_result


@dataclass(frozen=True, slots=True)
class CycleResult:
    """The observable output of one Noorvision cycle."""

    step: AgentStep
    action_result: ActionResult


def run_cycle(agent: NoorvisionAgent) -> CycleResult:
    """Observe, execute a local action, and close an experiment-learning loop."""
    step = agent.observe()
    action_result = execute_action(agent.memory_store, step.decision.action)

    if step.decision.action == "run_next_experiment":
        experiment = Experiment(
            hypothesis="Validate the next explicit Noorvision hypothesis.",
            success_criteria="A local experiment result is produced and stored as memory.",
        )
        result = run_experiment(experiment)
        memory = remember_result(experiment, result)
        agent.memory_store.add(memory)

    return CycleResult(step=step, action_result=action_result)
