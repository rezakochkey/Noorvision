"""Small, dependency-free memory primitives for Noorvision."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class MemoryKind(StrEnum):
    PROJECT = "project"
    DECISION = "decision"
    EXPERIMENT = "experiment"
    RESULT = "result"


@dataclass(frozen=True, slots=True)
class Memory:
    """A single durable fact or event Noorvision may need to recall."""

    kind: MemoryKind
    title: str
    content: str
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("title must not be empty")
        if not self.content.strip():
            raise ValueError("content must not be empty")
