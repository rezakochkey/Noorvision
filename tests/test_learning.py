import pytest

from noorvision.experiment import Experiment, ExperimentResult
from noorvision.learning import remember_result
from noorvision.memory import MemoryKind


def test_experiment_result_becomes_memory() -> None:
    experiment = Experiment("Tests pass", "CI is green")
    result = ExperimentResult(experiment.id, True, "The test suite passed.")

    memory = remember_result(experiment, result)

    assert memory.kind is MemoryKind.RESULT
    assert "successful" in memory.title
    assert memory.content == "The test suite passed."


def test_result_for_another_experiment_is_rejected() -> None:
    first = Experiment("First", "Criterion")
    second = Experiment("Second", "Criterion")
    result = ExperimentResult(first.id, False, "It failed.")

    with pytest.raises(ValueError, match="does not belong"):
        remember_result(second, result)
