"""Read party names from a 'between A and B' recital. Not legal advice."""
from __future__ import annotations

import json
import re

BETWEEN_RE = re.compile(
    r"between\s+(?P<a>.+?)\s+\(\"(?P<arole>[^\"]+)\"\)\s+and\s+(?P<b>.+?)\s+\(\"(?P<brole>[^\"]+)\"\)",
    re.IGNORECASE | re.DOTALL,
)


def find_parties(text: str) -> list[dict[str, str]]:
    match = BETWEEN_RE.search(text)
    if not match:
        return []
    return [
        {"name": " ".join(match.group("a").split()), "role": match.group("arole").strip()},
        {"name": " ".join(match.group("b").split()), "role": match.group("brole").strip()},
    ]


def render(parties: list[dict[str, str]]) -> str:
    return json.dumps(parties, indent=2) + "\n"
