"""Test"""
import pytest
from money import transfer_money, select_transaction
from person import Person

def test_transfer_money(monkeypatch):
    person = Person('Test', 'password', 50.00)
    inputs = iter(['A', '10', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 40.00

    inputs = iter(['E', '10', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 50.00

def test_select_transaction(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    assert select_transaction() == 'A'

    monkeypatch.setattr('builtins.input', lambda _: 'Z')
    assert select_transaction() == 'Z'

if __name__ == '__main__':
    pytest.main()
