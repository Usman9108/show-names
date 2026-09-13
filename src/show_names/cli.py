from __future__ import annotations

import argparse
import sys
from typing import Optional, Sequence

from .core import read_names


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="show-names",
        description="Print first and last names from a CSV file.",
    )
    parser.add_argument(
        "csv_path",
        nargs="?",
        default="examples/MOCK_DATA.csv",
        help="Path to a CSV file with first_name/last_name columns "
        "(default: examples/MOCK_DATA.csv)",
    )
    args = parser.parse_args(argv)

    try:
        for person in read_names(args.csv_path):
            print(person.first_name, person.last_name)
    except FileNotFoundError:
        print(f"error: no such file: {args.csv_path}", file=sys.stderr)
        return 1
    except KeyError as exc:
        print(f"error: CSV is missing required column: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
