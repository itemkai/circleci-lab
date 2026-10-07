"""Тесты для app.py, запускаются командой pytest."""

import pytest

from app import add, divide, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero():
    # Проверяем, что при делении на ноль выбрасывается ValueError
    with pytest.raises(ValueError):
        divide(1, 0)
