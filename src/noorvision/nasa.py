"""Minimal, dependency-free client for NASA's APOD API."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import date
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class NASAAPIError(RuntimeError):
    """Raised when NASA APOD cannot be fetched or validated."""


@dataclass(frozen=True, slots=True)
class APOD:
    """Validated Astronomy Picture of the Day response."""

    date: str
    title: str
    explanation: str
    media_type: str
    url: str
    hdurl: str | None = None


class NASAClient:
    """Small NASA API client using ``NASA_API_KEY`` from the environment."""

    BASE_URL = "https://api.nasa.gov/planetary/apod"

    def __init__(self, api_key: str | None = None, timeout: float = 10.0) -> None:
        self._api_key = api_key or os.getenv("NASA_API_KEY")
        self._timeout = timeout
        if not self._api_key:
            raise ValueError("NASA API key is required via NASA_API_KEY")

    def get_apod(self, day: date | None = None) -> APOD:
        """Fetch and validate one APOD record."""
        params = {"api_key": self._api_key}
        if day is not None:
            params["date"] = day.isoformat()

        request = Request(
            f"{self.BASE_URL}?{urlencode(params)}",
            headers={"Accept": "application/json", "User-Agent": "noorvision/0.1"},
        )
        try:
            with urlopen(request, timeout=self._timeout) as response:
                payload = json.load(response)
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise NASAAPIError("NASA APOD request failed") from exc

        if not isinstance(payload, dict):
            raise NASAAPIError("NASA APOD response must be a JSON object")

        required = ("date", "title", "explanation", "media_type", "url")
        if any(not isinstance(payload.get(field), str) or not payload[field].strip() for field in required):
            raise NASAAPIError("NASA APOD response is missing required fields")

        if payload["media_type"] not in {"image", "video"}:
            raise NASAAPIError("NASA APOD response has an unsupported media_type")

        hdurl = payload.get("hdurl")
        if hdurl is not None and not isinstance(hdurl, str):
            raise NASAAPIError("NASA APOD hdurl must be a string when present")

        return APOD(
            date=payload["date"],
            title=payload["title"],
            explanation=payload["explanation"],
            media_type=payload["media_type"],
            url=payload["url"],
            hdurl=hdurl,
        )
