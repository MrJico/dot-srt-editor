import json
from os import path

from constants import LANGUAGE

strings = json.loads(
    open(
        path.join(
            path.dirname(__file__),
            'strings', f'{LANGUAGE}.json',
        ),
    ).read(),
)


def get(key: str) -> str:
    return strings[key] if key in strings else f'Missing string {key} in language {LANGUAGE}'
