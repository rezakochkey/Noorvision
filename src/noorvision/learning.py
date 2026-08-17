"""Bridge experiment outcomes into Noorvision memory."""

from .experiment import Experiment, ExperimentResult
from .memory import Memory, MemoryKind


def remember_result(experiment: Experiment, result: ExperimentResult) -> Memory:
    """Turn a validated experiment outcome into durable memory data."""
    if result.experiment_id != experiment.id:
        raise ValueError("result does not belong to the supplied experiment")

    outcome = "successful" if result.successful else "unsuccessful"
    return Memory(
        kind=MemoryKind.RESULT,
        title=f"Experiment result: {outcome}",
        content=result.summary,
    )
