from datetime import datetime, timezone

import pytest

from noorvision.memory import Memory, MemoryKind


def test_memory_has_identity_and_utc_timestamp() -> None:
    memory = Memory(MemoryKind.DECISION, "Choose Python", "Use Python 3.11+ for the first implementation.")

    assert memory.kind is MemoryKind.DECISION
    assert memory.title == "Choose Python"
    assert memory.content
    assert memory.created_at.tzinfo is timezone.utc
    assert memory.id is not None


def test_memory_rejects_empty_title() -> None:
    with pytest.raises(ValueError, match="title"):
        Memory(MemoryKind.PROJECT, "  ", "A valid description")


def test_memory_rejects_empty_content() -> None:
    with pytest.raises(ValueError, match="content"):
        Memory(MemoryKind.RESULT, "A result", "  ")
