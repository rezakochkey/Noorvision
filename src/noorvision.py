"""Minimal Noorvision core.

The first implementation is deliberately small: it provides a structured
project-health snapshot that can later become a foundation for larger
capabilities.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ProjectStatus:
    """Describe the current state of a Noorvision project."""

    name: str
    phase: str
    next_action: str


def status(name: str, phase: str, next_action: str) -> ProjectStatus:
    """Create a validated project status record."""
    values = {"name": name, "phase": phase, "next_action": next_action}
    if any(not isinstance(value, str) or not value.strip() for value in values.values()):
        raise ValueError("name, phase, and next_action must be non-empty strings")

    return ProjectStatus(
        name=name.strip(),
        phase=phase.strip(),
        next_action=next_action.strip(),
    )
