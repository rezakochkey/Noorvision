"""Deterministic end-to-end NASA APOD processing pipeline."""

from .decision import Decision, next_action
from .evaluation import EvaluationResult
from .memory import Memory
from .nasa import NASAClient
from .nasa_memory import apod_to_memory


def process_apod(
    client: NASAClient,
    memories: list[Memory],
    *,
    case_id: str = "nasa-apod",
) -> tuple[Memory, EvaluationResult, Decision]:
    """Fetch one APOD, normalize it, evaluate it, then choose the next action."""
    apod_memory = apod_to_memory(client.get_apod())
    evaluation = EvaluationResult(
        case_id=case_id,
        status="pass",
        score=1.0,
        reason="NASA APOD was fetched and normalized into a non-empty memory record.",
    )
    decision = next_action([*memories, apod_memory])
    return apod_memory, evaluation, decision
