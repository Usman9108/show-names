from show_names.core import Person, read_names


def test_read_names(tmp_path):
    csv_path = tmp_path / "people.csv"
    csv_path.write_text(
        "id,first_name,last_name,email\n"
        "1,Ada,Lovelace,ada@example.com\n"
        "2,Alan,Turing,alan@example.com\n",
        encoding="utf-8",
    )

    assert list(read_names(csv_path)) == [
        Person("Ada", "Lovelace"),
        Person("Alan", "Turing"),
    ]


def test_read_names_missing_file(tmp_path):
    missing = tmp_path / "does-not-exist.csv"
    try:
        list(read_names(missing))
        assert False, "expected FileNotFoundError"
    except FileNotFoundError:
        pass
