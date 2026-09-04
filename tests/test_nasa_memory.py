from noorvision.memory import MemoryKind
from noorvision.nasa import APOD
from noorvision.nasa_memory import apod_to_memory


def test_apod_to_memory_normalizes_valid_apod() -> None:
    apod = APOD(
        date="2026-09-04",
        title="A Bright Nebula",
        explanation="A nebula shines across the sky.",
        media_type="image",
        url="https://example.test/apod.jpg",
        hdurl="https://example.test/apod-hd.jpg",
    )

    memory = apod_to_memory(apod)

    assert memory.kind is MemoryKind.RESULT
    assert memory.title == "NASA APOD: A Bright Nebula"
    assert "A nebula shines across the sky." in memory.content
    assert "Media: image" in memory.content
    assert "https://example.test/apod.jpg" in memory.content


def test_apod_to_memory_preserves_video_media_type() -> None:
    apod = APOD(
        date="2026-09-04",
        title="A Space Video",
        explanation="A short space video.",
        media_type="video",
        url="https://example.test/apod.mp4",
    )

    memory = apod_to_memory(apod)

    assert memory.kind is MemoryKind.RESULT
    assert "Media: video" in memory.content
    assert "https://example.test/apod.mp4" in memory.content
