from dataclasses import FrozenInstanceError

import pytest

from noorvision.evaluation import EvaluationResult


def test_evaluation_result_represents_a_passing_outcome() -> None:
    result = EvaluationResult(
        case_id="case-001",
        status="pass",
        score=1.0,
        reason="Exact expected output matched.",
    )

    assert result.passed is True
    assert result.status == "pass"
    assert result.score == 1.0


def test_evaluation_result_can_represent_failure_without_hiding_it() -> None:
    result = EvaluationResult(
        case_id="case-002",
        status="fail",
        score=0.0,
        reason="Observed output did not match the expected outcome.",
    )

    assert result.passed is False
    assert result.status == "fail"
    assert result.reason != ""


def test_evaluation_result_is_immutable() -> None:
    result = EvaluationResult(
        case_id="case-003",
        status="pass",
        score=0.5,
        reason="Partial rubric score.",
    )

    with pytest.raises(FrozenInstanceError):
        result.score = 1.0  # type: ignore[misc]


@pytest.mark.parametrize("score", [-0.01, 1.01])
def test_evaluation_result_rejects_scores_outside_range(score: float) -> None:
    with pytest.raises(ValueError, match="score must be between"):
        EvaluationResult(
            case_id="case-invalid",
            status="fail",
            score=score,
            reason="Invalid score.",
        )
