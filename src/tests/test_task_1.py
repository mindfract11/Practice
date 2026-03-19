import pytest

from task_1.solution import main

SEPARATOR = "-" * 40


def run_main(monkeypatch, capsys, inputs: list[str]) -> list[str]:
    """
    Replaces built-in input() with values from the inputs list, runs main(),
    and returns stdout split into individual lines.
    """
    values = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(values))
    main()
    output = capsys.readouterr().out
    return output.splitlines()


# ---------------------------------------------------------------------------
# Sample 1: Julia orders 3 portions at 75.5 credits each
# ---------------------------------------------------------------------------


def test_sample_1(monkeypatch, capsys):
    lines = run_main(monkeypatch, capsys, ["Julia", "3", "75.5"])
    assert lines[0] == SEPARATOR
    assert lines[1] == "Hello, Julia! Welcome to the Cosmic Cafe!"
    assert lines[2] == "Portions ordered: 3"
    assert lines[3] == "Price per portion: 75.5 credits"
    assert lines[4] == "Total: 226.50 credits"
    assert lines[5] == SEPARATOR


# ---------------------------------------------------------------------------
# Sample 2: Max orders 2 portions at 10.0 credits each
# ---------------------------------------------------------------------------


def test_sample_2(monkeypatch, capsys):
    lines = run_main(monkeypatch, capsys, ["Max", "2", "10.0"])
    assert lines[0] == SEPARATOR
    assert lines[1] == "Hello, Max! Welcome to the Cosmic Cafe!"
    assert lines[2] == "Portions ordered: 2"
    assert lines[3] == "Price per portion: 10.0 credits"
    assert lines[4] == "Total: 20.00 credits"
    assert lines[5] == SEPARATOR


# ---------------------------------------------------------------------------
# Sample 3: Oleg orders 10 portions at 9.99 credits each
# ---------------------------------------------------------------------------


def test_sample_3(monkeypatch, capsys):
    lines = run_main(monkeypatch, capsys, ["Oleg", "10", "9.99"])
    assert lines[0] == SEPARATOR
    assert lines[1] == "Hello, Oleg! Welcome to the Cosmic Cafe!"
    assert lines[2] == "Portions ordered: 10"
    assert lines[3] == "Price per portion: 9.99 credits"
    assert lines[4] == "Total: 99.90 credits"
    assert lines[5] == SEPARATOR


# ---------------------------------------------------------------------------
# Output structure: exactly 6 lines
# ---------------------------------------------------------------------------


def test_output_has_exactly_6_lines(monkeypatch, capsys):
    lines = run_main(monkeypatch, capsys, ["Julia", "3", "75.5"])
    assert len(lines) == 6, f"Expected 6 lines of output, got {len(lines)}"


# ---------------------------------------------------------------------------
# Output structure: first and last lines are separators of 40 dashes
# ---------------------------------------------------------------------------


def test_separators_are_40_dashes(monkeypatch, capsys):
    lines = run_main(monkeypatch, capsys, ["Julia", "3", "75.5"])
    assert lines[0] == SEPARATOR, "First line must be exactly 40 dashes"
    assert lines[5] == SEPARATOR, "Last line must be exactly 40 dashes"


# ---------------------------------------------------------------------------
# Total formatting: must always show exactly 2 decimal places
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "count,price,expected_total",
    [
        ("1", "50.0", "50.00"),
        ("4", "25.25", "101.00"),
        ("1000", "9.99", "9990.00"),
        ("2", "0.01", "0.02"),
        ("1", "0.01", "0.01"),
    ],
)
def test_total_formatting(monkeypatch, capsys, count, price, expected_total):
    lines = run_main(monkeypatch, capsys, ["TestUser", count, price])
    assert lines[4] == f"Total: {expected_total} credits", (
        f"For {count} x {price}: expected 'Total: {expected_total} credits', got '{lines[4]}'"
    )


# ---------------------------------------------------------------------------
# Name handling: name appears verbatim on the greeting line
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("name", ["Anna", "Bohdan", "Christina", "Oleksiy", "J"])
def test_name_on_greeting_line(monkeypatch, capsys, name):
    lines = run_main(monkeypatch, capsys, [name, "1", "10.0"])
    assert lines[1] == f"Hello, {name}! Welcome to the Cosmic Cafe!"


# ---------------------------------------------------------------------------
# Count: integer value appears verbatim on the portions line
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("count", ["1", "42", "999", "1000"])
def test_count_on_portions_line(monkeypatch, capsys, count):
    lines = run_main(monkeypatch, capsys, ["TestUser", count, "1.0"])
    assert lines[2] == f"Portions ordered: {count}"


# ---------------------------------------------------------------------------
# Price: float value appears verbatim on the price line
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("price", ["0.01", "9999.99", "1.5", "100.0"])
def test_price_on_price_line(monkeypatch, capsys, price):
    lines = run_main(monkeypatch, capsys, ["TestUser", "1", price])
    assert lines[3] == f"Price per portion: {price} credits"


# ---------------------------------------------------------------------------
# Input: must be called exactly 3 times
# ---------------------------------------------------------------------------


def test_input_called_exactly_three_times(monkeypatch):
    call_count = 0

    def fake_input(_):
        nonlocal call_count
        call_count += 1
        return ["TestUser", "2", "10.0"][call_count - 1]

    monkeypatch.setattr("builtins.input", fake_input)
    main()
    assert call_count == 3, f"input() must be called exactly 3 times, got {call_count}"
