"""Experiment primitives for Noorvision's learning loop."""

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Experiment:
    """A small, explicit hypothesis Noorvision can validate."""

    hypothesis: str
    success_criteria: str
    id: UUID = uuid4()

    def __post_init__(self) -> None:
        if not self.hypothesis.strip():
            raise ValueError("hypothesis must not be empty")
        if not self.success_criteria.strip():
            raise ValueError("success_criteria must not be empty")


@dataclass(frozen=True, slots=True)
class ExperimentResult:
    """The recorded outcome of an experiment."""

    experiment_id: UUID
    successful: bool
    summary: str

    def __post_init__(self) -> None:
        if not self.summary.strip():
            raise ValueError("summary must not be empty")
