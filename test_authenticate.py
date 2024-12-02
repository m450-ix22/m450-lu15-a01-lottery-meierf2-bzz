import pytest
from authenticate import login, load_people
from person import Person

def test_load_people():
    people = load_people()
    assert len(people) == 3
    assert isinstance(people[0], Person)

def test_login(monkeypatch):
    people = load_people()
    monkeypatch.setattr('builtins.input', lambda _: 'geheim')
    person = login()
    assert person == people[0]

    # Mock input to simulate incorrect password and then correct password
    inputs = iter(['wrongpassword', 'geheim'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    person = login()
    assert person == people[0]

if __name__ == '__main__':
    pytest.main()