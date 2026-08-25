from pathlib import Path


PROTOCOL = Path(__file__).parents[1] / "docs" / "NOORVISION_EVALUATION_PROTOCOL.md"


def test_evaluation_protocol_exists():
    assert PROTOCOL.is_file()


def test_evaluation_protocol_requires_neutrality_and_self_evaluation():
    text = PROTOCOL.read_text(encoding="utf-8")
    assert "**Neutrality**" in text
    assert "**Self-evaluation**" in text
    assert "NOORVISION is an evaluation subject as well as an evaluator." in text


def test_evaluation_protocol_requires_evidence_over_llm_judgment():
    text = PROTOCOL.read_text(encoding="utf-8")
    assert "**Evidence first**" in text
    assert "A model-generated judgment is evidence, not unquestionable ground truth." in text
    assert "exact ground-truth comparison" in text
    assert "executable tests / validators" in text


def test_evaluation_protocol_allows_failure_and_forbids_hidden_semantic_assumptions():
    text = PROTOCOL.read_text(encoding="utf-8")
    assert "**Failure is valid**" in text
    assert "**No hidden semantic assumptions**" in text
    assert "Abjad" in text


def test_evaluation_protocol_records_reproducibility_fields():
    text = PROTOCOL.read_text(encoding="utf-8")
    for field in (
        "task identifier and version",
        "evaluated system and model/version",
        "tool access and environment",
        "time/token/attempt budget",
        "final score and failure reasons",
    ):
        assert field in text
