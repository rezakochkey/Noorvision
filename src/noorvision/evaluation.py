"""Core value objects for NOORVISION evaluation results."""

from dataclasses import dataclass
from typing import Literal


EvaluationStatus = Literal["pass", "fail"]


@dataclass(frozen=True, slots=True)
class EvaluationResult:
    """Immutable outcome of evaluating one case."""

    case_id: str
    status: EvaluationStatus
    score: float
    reason: str

    def __post_init__(self) -> None:
        if not self.case_id:
            raise ValueError("case_id must not be empty")
        if not 0.0 <= self.score <= 1.0:
            raise ValueError("score must be between 0.0 and 1.0")
        if not self.reason:
            raise ValueError("reason must not be empty")

    @property
    def passed(self) -> bool:
        """Return whether this evaluation passed."""
        return self.status == "pass"
