"""Safe local experiment execution for Noorvision."""

from .experiment import Experiment, ExperimentResult


def run_experiment(experiment: Experiment) -> ExperimentResult:
    """Run the current deterministic experiment contract.

    This first runner does not execute arbitrary code. It records that the
    experiment was accepted by the local runner, leaving real integrations
    for a later, explicitly configured layer.
    """
    return ExperimentResult(
        experiment_id=experiment.id,
        successful=True,
        summary=(
            f"Experiment accepted by the local runner: {experiment.hypothesis}. "
            f"Success criterion recorded: {experiment.success_criteria}."
        ),
    )
