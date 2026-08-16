import pytest

from noorvision import ProjectStatus, status


def test_status_creates_normalized_project_status():
    result = status("  Noorvision  ", " foundation ", " define MVP ")

    assert result == ProjectStatus("Noorvision", "foundation", "define MVP")


def test_status_rejects_empty_values():
    with pytest.raises(ValueError):
        status("Noorvision", "", "define MVP")
