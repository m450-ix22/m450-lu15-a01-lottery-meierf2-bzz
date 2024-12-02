"""Test"""
import pytest
from menu import show_menu, select_menu

def test_show_menu(capsys):
    show_menu()
    captured = capsys.readouterr()
    assert 'Lotto' in captured.out

def test_select_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    assert select_menu() == 'A'

    monkeypatch.setattr('builtins.input', lambda _: 'Z')
    assert select_menu() == 'Z'

if __name__ == '__main__':
    pytest.main()
