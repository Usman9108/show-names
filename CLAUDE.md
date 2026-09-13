# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

`show-names` is a small installable Python package (src-layout) that reads `first_name`/`last_name` records out of a CSV file. It exposes both a library API (`show_names.read_names`) and a console-script CLI (`show-names`).

## Environment

The project uses a local virtual environment at `venv/` (Python 3.14, created with `python -m venv venv`), plus the package itself installed in editable mode.

- Activate (PowerShell): `.\venv\Scripts\Activate.ps1`
- Install/reinstall after changing `pyproject.toml`: `pip install -e ".[dev]"`

## Commands

- Run tests: `pytest` (or `python -m pytest`)
- Run a single test: `pytest tests/test_core.py::test_read_names`
- Run the CLI: `show-names examples/MOCK_DATA.csv` (defaults to that path if omitted)

There is no linter or build step beyond `pyproject.toml` (`setuptools` backend).

## Architecture

- `src/show_names/core.py` — the library API: `Person` (a `NamedTuple` of `first_name`/`last_name`) and `read_names(csv_path)`, a generator that yields one `Person` per CSV row. This is the single place CSV-parsing logic lives.
- `src/show_names/cli.py` — thin `argparse`-based wrapper around `core.read_names`; translates `FileNotFoundError`/`KeyError` into user-facing CLI error messages (exit code 1) rather than tracebacks.
- `src/show_names/__init__.py` — re-exports `Person` and `read_names` as the public package API.
- `examples/MOCK_DATA.csv` — sample data used as the CLI's default argument and referenced in the README; not used by tests.
- `tests/` — exercises `core.read_names` directly (not the CLI).

When changing the CSV schema handling (columns read, error behavior), update `core.py` only — both the CLI and any library consumers go through it.
