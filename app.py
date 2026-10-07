"""Простое приложение-калькулятор, которое проверяется тестами в CircleCI."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    # Деление на ноль запрещено - выбрасываем понятную ошибку
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b
