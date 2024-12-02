import pytest
from numeric_input import read_int, read_float

def test_read_int(monkeypatch):
    # Test mit einer gültigen Eingabe
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert read_int('prompt', 1, 10) == 5

    # Test mit einer ungültigen Eingabe, die den Bereich überschreitet
    inputs = iter(['15', '5'])  # Erste Eingabe ist ungültig, zweite ist gültig
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_int('prompt', 1, 10) == 5


def test_read_float(monkeypatch):
    # Test mit einer gültigen Eingabe
    monkeypatch.setattr('builtins.input', lambda _: '5.5')
    assert read_float('prompt', 1.0, 10.0) == 5.5

    # Test mit einer ungültigen Eingabe, die den Bereich überschreitet
    inputs = iter(['15.5', '5.5'])  # Erste Eingabe ist ungültig, zweite ist gültig
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_float('prompt', 1.0, 10.0) == 5.5


if __name__ == '__main__':
    pytest.main()
