import json
from os import path

from constants import LANGUAGE

with open(
    path.join(
        path.dirname(__file__),
        "strings",
        f"{LANGUAGE}.json",
    ),
    encoding="utf-8",
) as jfile:
    strings = json.load(jfile)


def get(key: str) -> str:
    return (
        strings[key]
        if key in strings
        else f"Missing string {key} in language {LANGUAGE}"
    )
