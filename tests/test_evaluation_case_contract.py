from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationCase:
    case_id: str
    input_text: str
    expected_output: str


def evaluate_case(case: EvaluationCase, actual_output: str) -> bool:
    return actual_output == case.expected_output


def test_deterministic_evaluation_case_passes_exact_match():
    case = EvaluationCase(
        case_id="deterministic-001",
        input_text="What is 2 + 2?",
        expected_output="4",
    )
    assert evaluate_case(case, "4") is True


def test_deterministic_evaluation_case_rejects_wrong_output():
    case = EvaluationCase(
        case_id="deterministic-001",
        input_text="What is 2 + 2?",
        expected_output="4",
    )
    assert evaluate_case(case, "5") is False


def test_evaluation_case_identity_is_not_used_for_scoring():
    first = EvaluationCase("deterministic-001", "What is 2 + 2?", "4")
    second = EvaluationCase("deterministic-001", "What is 2 + 2?", "4")
    assert first == second
    assert evaluate_case(second, "4") is True
