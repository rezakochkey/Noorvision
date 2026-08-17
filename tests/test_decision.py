from noorvision.decision import next_action
from noorvision.memory import Memory, MemoryKind


def test_empty_memory_captures_context() -> None:
    decision = next_action([])

    assert decision.action == "capture_context"


def test_missing_project_context_is_detected() -> None:
    memories = [Memory(MemoryKind.RESULT, "Result", "A result")]

    decision = next_action(memories)

    assert decision.action == "define_project"


def test_project_without_decision_records_one() -> None:
    memories = [Memory(MemoryKind.PROJECT, "Noorvision", "Initial project")]

    decision = next_action(memories)

    assert decision.action == "record_decision"


def test_project_and_decision_lead_to_experiment() -> None:
    memories = [
        Memory(MemoryKind.PROJECT, "Noorvision", "Initial project"),
        Memory(MemoryKind.DECISION, "Use Python", "Use Python 3.11+"),
    ]

    decision = next_action(memories)

    assert decision.action == "run_next_experiment"
