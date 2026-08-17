import pytest

from noorvision.experiment import Experiment, ExperimentResult


def test_experiment_gets_a_unique_identity() -> None:
    first = Experiment("Test memory", "Tests pass")
    second = Experiment("Test memory", "Tests pass")

    assert first.id != second.id


def test_experiment_rejects_empty_hypothesis() -> None:
    with pytest.raises(ValueError, match="hypothesis"):
        Experiment("  ", "Tests pass")


def test_result_requires_summary() -> None:
    experiment = Experiment("Test memory", "Tests pass")

    with pytest.raises(ValueError, match="summary"):
        ExperimentResult(experiment.id, True, "  ")
