import json
from datetime import date

import pytest

from noorvision import nasa


class FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return json.dumps(self._payload).encode()

    def __iter__(self):
        return iter(())


def test_client_requires_api_key(monkeypatch):
    monkeypatch.delenv("NASA_API_KEY", raising=False)
    with pytest.raises(ValueError, match="NASA API key is required"):
        nasa.NASAClient()


def test_get_apod_uses_key_and_validates_response(monkeypatch):
    seen = {}
    payload = {
        "date": "2026-09-04",
        "title": "A Test Star",
        "explanation": "A useful fixture.",
        "media_type": "image",
        "url": "https://example.test/apod.jpg",
        "hdurl": "https://example.test/apod-hd.jpg",
    }

    def fake_urlopen(request, timeout):
        seen["url"] = request.full_url
        seen["timeout"] = timeout
        return FakeResponse(payload)

    monkeypatch.setattr(nasa, "urlopen", fake_urlopen)
    result = nasa.NASAClient(api_key="test-secret", timeout=3.5).get_apod(date(2026, 9, 4))

    assert result.title == "A Test Star"
    assert result.media_type == "image"
    assert "api_key=test-secret" in seen["url"]
    assert "date=2026-09-04" in seen["url"]
    assert seen["timeout"] == 3.5


def test_get_apod_rejects_invalid_media_type(monkeypatch):
    payload = {
        "date": "2026-09-04",
        "title": "Bad Fixture",
        "explanation": "Invalid media type.",
        "media_type": "audio",
        "url": "https://example.test/apod",
    }
    monkeypatch.setattr(nasa, "urlopen", lambda request, timeout: FakeResponse(payload))

    with pytest.raises(nasa.NASAAPIError, match="unsupported media_type"):
        nasa.NASAClient(api_key="test-secret").get_apod()


def test_get_apod_never_requires_live_nasa(monkeypatch):
    def fail_if_called(*args, **kwargs):
        raise AssertionError("live NASA request must not run in unit tests")

    monkeypatch.setattr(nasa, "urlopen", fail_if_called)
    # Constructor validation is local and must remain usable without network access.
    client = nasa.NASAClient(api_key="test-secret")
    assert client._api_key == "test-secret"
