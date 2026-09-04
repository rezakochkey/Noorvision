"""Normalize NASA APOD records into Noorvision memory objects."""

from .memory import Memory, MemoryKind
from .nasa import APOD


def apod_to_memory(apod: APOD) -> Memory:
    """Convert one validated APOD record into durable project memory."""
    content = f"{apod.explanation}\nMedia: {apod.media_type}\nURL: {apod.url}"
    return Memory(
        kind=MemoryKind.RESULT,
        title=f"NASA APOD: {apod.title}",
        content=content,
    )
