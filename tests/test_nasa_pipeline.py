from datetime import date

from noorvision.decision import Decision
from noorvision.evaluation import EvaluationResult
from noorvision.memory import Memory, MemoryKind
from noorvision.nasa import APOD
from noorvision.nasa_pipeline import process_apod


class FakeNASAClient:
    def get_apod(self) -> APOD:
        return APOD(
            date=date(2026, 9, 4).isoformat(),
            title="A Bright Nebula",
            explanation="A nebula shines across the sky.",
            media_type="image",
            url="https://example.test/apod.jpg",
        )


def test_process_apod_flows_nasa_to_memory_evaluation_and_decision() -> None:
    project = Memory(
        kind=MemoryKind.PROJECT,
        title="NOORVISION",
        content="NASA integration experiment",
    )
    decision = Memory(
        kind=MemoryKind.DECISION,
        title="Use NASA APOD",
        content="Validate the public data path.",
    )

    memory, evaluation, next_decision = process_apod(
        FakeNASAClient(), [project, decision], case_id="brick-42"
    )

    assert memory.kind is MemoryKind.RESULT
    assert memory.title == "NASA APOD: A Bright Nebula"
    assert evaluation == EvaluationResult(
        case_id="brick-42",
        status="pass",
        score=1.0,
        reason="NASA APOD was fetched and normalized into a non-empty memory record.",
    )
    assert next_decision == Decision(
        action="run_next_experiment",
        reason="Project context and at least one decision are recorded; validate the next hypothesis.",
    )


def test_process_apod_does_not_call_live_nasa() -> None:
    memory, evaluation, next_decision = process_apod(FakeNASAClient(), [])

    assert memory.kind is MemoryKind.RESULT
    assert evaluation.passed
    assert next_decision.action == "capture_context"
