from noorvision.experiment import Experiment
from noorvision.experiment_runner import run_experiment


def test_runner_returns_result_for_experiment() -> None:
    experiment = Experiment(
        "The local runner can accept an explicit hypothesis",
        "A result is returned with the same experiment id",
    )

    result = run_experiment(experiment)

    assert result.experiment_id == experiment.id
    assert result.successful is True
    assert "accepted by the local runner" in result.summary
