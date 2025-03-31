import os

import pytest

# Импортируем функцию my_function из вашего модуля
from test_poetry.src.decorators import log, my_function


# Тест для проверки успешного выполнения функции
def test_my_function_success(capsys):
    result = my_function(1, 2)
    assert result == 3  # Проверяем, что функция возвращает правильный результат

    # Проверяем, что в stdout выводится сообщение об успешном выполнении
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out

# Тест для проверки обработки ошибок
def test_my_function_error(capsys):
    # Вызываем функцию с некорректными аргументами, чтобы вызвать ошибку
    result = my_function("1", 2)

    # Проверяем, что в stdout выводится сообщение об ошибке
    captured = capsys.readouterr()
    assert "my_function ошибка" in captured.out
    assert "Inputs: (('1', 2), {})" in captured.out

# Тест для проверки записи логов в файл
def test_my_function_log_to_file(tmpdir):
    # Создаем временный файл для логов
    log_file = tmpdir.join("log.txt")

    # Применяем декоратор с указанием файла для логов
    @log(filename=log_file)
    def my_function_with_log(x, y):
        return x + y

    # Вызываем функцию
    result = my_function_with_log(1, 2)
    assert result == 3

    # Проверяем, что в файл записано сообщение об успешном выполнении
    assert log_file.read() == "my_function_with_log ok"

    # Вызываем функцию с ошибкой
    my_function_with_log("1", 2)

    # Проверяем, что в файл записано сообщение об ошибке
    assert "my_function_with_log ошибка" in log_file.read()
    assert "Inputs: (('1', 2), {})" in log_file.read()

# Тест для проверки, что функция возвращает None при ошибке
def test_my_function_returns_none_on_error():
    result = my_function("1", 2)
    assert result is None
