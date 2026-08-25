from noorvision.evaluation_models import EvaluationCase
from noorvision.evaluator import evaluate_case


def test_evaluator_returns_pass_for_exact_match():
    case = EvaluationCase(case_id="case-001", expected=4, actual=4)

    result = evaluate_case(case)

    assert result.case_id == "case-001"
    assert result.passed is True
    assert result.score == 1.0
    assert result.reason == "exact match"


def test_evaluator_returns_fail_for_mismatch():
    case = EvaluationCase(case_id="case-002", expected=4, actual=5)

    result = evaluate_case(case)

    assert result.case_id == "case-002"
    assert result.passed is False
    assert result.score == 0.0
    assert result.reason == "actual value does not match expected value"


def test_evaluator_rejects_empty_case_id():
    case = EvaluationCase(case_id="", expected=4, actual=4)

    try:
        evaluate_case(case)
    except ValueError as exc:
        assert str(exc) == "case_id must not be empty"
    else:
        raise AssertionError("evaluate_case must reject an empty case_id")
