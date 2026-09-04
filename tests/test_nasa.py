import json
from datetime import date
from urllib.error import HTTPError, URLError

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


class MalformedResponse(FakeResponse):
    def read(self):
        return b"{not-valid-json"


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


def test_get_apod_maps_http_429_to_nasa_api_error(monkeypatch):
    monkeypatch.setattr(
        nasa,
        "urlopen",
        lambda request, timeout: (_ for _ in ()).throw(
            HTTPError(request.full_url, 429, "rate limited", {}, None)
        ),
    )

    with pytest.raises(nasa.NASAAPIError, match="NASA APOD request failed") as exc_info:
        nasa.NASAClient(api_key="test-secret").get_apod()

    assert "test-secret" not in str(exc_info.value)


def test_get_apod_maps_http_5xx_to_nasa_api_error(monkeypatch):
    monkeypatch.setattr(
        nasa,
        "urlopen",
        lambda request, timeout: (_ for _ in ()).throw(
            HTTPError(request.full_url, 503, "service unavailable", {}, None)
        ),
    )

    with pytest.raises(nasa.NASAAPIError, match="NASA APOD request failed"):
        nasa.NASAClient(api_key="test-secret").get_apod()


def test_get_apod_maps_network_failure_to_nasa_api_error(monkeypatch):
    monkeypatch.setattr(
        nasa,
        "urlopen",
        lambda request, timeout: (_ for _ in ()).throw(URLError("connection refused")),
    )

    with pytest.raises(nasa.NASAAPIError, match="NASA APOD request failed"):
        nasa.NASAClient(api_key="test-secret").get_apod()


def test_get_apod_maps_timeout_to_nasa_api_error(monkeypatch):
    monkeypatch.setattr(
        nasa,
        "urlopen",
        lambda request, timeout: (_ for _ in ()).throw(TimeoutError("timed out")),
    )

    with pytest.raises(nasa.NASAAPIError, match="NASA APOD request failed"):
        nasa.NASAClient(api_key="test-secret").get_apod()


def test_get_apod_maps_malformed_json_to_nasa_api_error(monkeypatch):
    monkeypatch.setattr(nasa, "urlopen", lambda request, timeout: MalformedResponse(None))

    with pytest.raises(nasa.NASAAPIError, match="NASA APOD request failed"):
        nasa.NASAClient(api_key="test-secret").get_apod()


def test_get_apod_rejects_missing_required_fields(monkeypatch):
    payload = {
        "date": "2026-09-04",
        "title": "Incomplete Fixture",
        "media_type": "image",
        "url": "https://example.test/apod.jpg",
    }
    monkeypatch.setattr(nasa, "urlopen", lambda request, timeout: FakeResponse(payload))

    with pytest.raises(nasa.NASAAPIError, match="missing required fields"):
        nasa.NASAClient(api_key="test-secret").get_apod()


def test_get_apod_rejects_non_string_hdurl(monkeypatch):
    payload = {
        "date": "2026-09-04",
        "title": "Bad HD Fixture",
        "explanation": "Invalid hdurl type.",
        "media_type": "image",
        "url": "https://example.test/apod.jpg",
        "hdurl": 123,
    }
    monkeypatch.setattr(nasa, "urlopen", lambda request, timeout: FakeResponse(payload))

    with pytest.raises(nasa.NASAAPIError, match="hdurl must be a string"):
        nasa.NASAClient(api_key="test-secret").get_apod()
