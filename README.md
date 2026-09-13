# show-names

Read `first_name`/`last_name` records out of a CSV file, as a Python library or a command-line tool.

## Install

```bash
pip install -e .
```

(This installs it in "editable" mode from a local checkout. Once published to PyPI, it would just be `pip install show-names`.)

## Use as a library

```python
from show_names import read_names

for person in read_names("examples/MOCK_DATA.csv"):
    print(person.first_name, person.last_name)
```

`read_names(csv_path)` returns an iterator of `Person` namedtuples (`.first_name`, `.last_name`). It raises `FileNotFoundError` if the path doesn't exist, and `KeyError` if the CSV is missing a `first_name` or `last_name` column.

The input CSV needs at least `first_name` and `last_name` columns; other columns (id, email, etc.) are ignored.

## Use as a CLI

```bash
show-names examples/MOCK_DATA.csv
```

Ada Lovelace
Alan Turing
...

If no path is given, it defaults to `examples/MOCK_DATA.csv`.

## Development

```bash
pip install -e ".[dev]"
pytest
```

## Project layout

- `src/show_names/core.py` — the `read_names()` / `Person` library API.
- `src/show_names/cli.py` — the `show-names` command-line entry point.
- `examples/MOCK_DATA.csv` — sample data for trying it out.
- `tests/` — pytest tests for the library API.

## License

MIT — see [LICENSE](LICENSE).
