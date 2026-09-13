from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterator, NamedTuple, Union


class Person(NamedTuple):
    first_name: str
    last_name: str


def read_names(csv_path: Union[str, Path]) -> Iterator[Person]:
    """Yield a ``Person`` for each row of a CSV file.

    The file must have ``first_name`` and ``last_name`` columns (extra
    columns are ignored).

    Raises:
        FileNotFoundError: if ``csv_path`` does not exist.
        KeyError: if the CSV is missing a required column.
    """
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield Person(row["first_name"], row["last_name"])
