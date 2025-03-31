from datetime import datetime, time
from unittest.mock import mock_open, patch

import pandas as pd
import pytest
import requests_mock
import yfinance as yf

from test_poetry.src.utils import filtered_data_by_date, get_currency_stocks, get_exchange_rate


# Тесты для функции filtered_data_by_date
def test_filtered_data_by_date():
    # Создаем тестовые данные
    data = {
        "Дата операции": [
            "2021-12-01 10:00:00",  # Должна быть включена
            "2021-12-15 12:00:00",  # Должна быть включена
            "2022-01-01 14:00:00",  # Должна быть исключена
        ],
        "Сумма": [100, 200, 300],
    }
    df = pd.DataFrame(data)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"])

    # Мокируем чтение файла
    with patch("pandas.read_excel", return_value=df):
        result = filtered_data_by_date("dummy_path.xls", "2021-12-31 23:59:59")

    # Проверяем результат
    assert len(result) == 1  # Ожидаем 2 строки
    assert all(result["Дата операции"] <= datetime(2021, 12, 31, 23, 59, 59))


# Тесты для функции get_currency_stocks
def test_get_currency_stocks(requests_mock):
    # Мокируем файл с настройками
    mock_settings = '{"user_currencies": ["USD", "EUR"]}'
    with patch("builtins.open", mock_open(read_data=mock_settings)):
        # Мокируем API запрос
        requests_mock.get(
            "https://v6.exchangerate-api.com/v6/None/latest/USD",  # Используем API_KEY=None
            json={"conversion_rates": {"RUB": 75.5}},
        )
        requests_mock.get(
            "https://v6.exchangerate-api.com/v6/None/latest/EUR",  # Используем API_KEY=None
            json={"conversion_rates": {"RUB": 85.5}},
        )

        # Вызываем функцию
        result = get_currency_stocks("dummy_path.json")

    # Проверяем результат
    assert len(result) == 2
    assert result[0]["currency"] == "USD"
    assert result[0]["rate"] == 75.5
    assert result[1]["currency"] == "EUR"
    assert result[1]["rate"] == 85.5


# Тесты для функции get_exchange_rate
def test_get_exchange_rate():
    # Мокируем файл с настройками
    mock_settings = '{"user_stocks": ["AAPL", "GOOGL"]}'
    with patch("builtins.open", mock_open(read_data=mock_settings)):
        # Мокируем yfinance
        mock_data_aapl = pd.DataFrame(
            {"Close": [150.0]},
            index=[pd.Timestamp("2023-01-01")],
        )
        mock_data_googl = pd.DataFrame(
            {"Close": [2800.0]},
            index=[pd.Timestamp("2023-01-01")],
        )
        with patch("yfinance.Ticker") as mock_ticker:
            # Настраиваем mock_ticker для возврата разных данных для каждого тикера
            mock_ticker.side_effect = [
                type("MockTicker", (), {"history": lambda *args, **kwargs: mock_data_aapl}),
                type("MockTicker", (), {"history": lambda *args, **kwargs: mock_data_googl}),
            ]

            # Вызываем функцию
            result = get_exchange_rate("dummy_path.json")

    # Проверяем результат
    assert len(result) == 2
    assert result[0]["stock"] == "AAPL"
    assert result[0]["price"] == 150.0
    assert result[1]["stock"] == "GOOGL"
    assert result[1]["price"] == 2800.0


# Тест для обработки ошибок в get_currency_stocks
def test_get_currency_stocks_error(requests_mock):
    # Мокируем файл с настройками
    mock_settings = '{"user_currencies": ["USD"]}'
    with patch("builtins.open", mock_open(read_data=mock_settings)):
        # Мокируем ошибку API
        requests_mock.get(
            "https://v6.exchangerate-api.com/v6/None/latest/USD",  # Используем API_KEY=None
            status_code=500,
        )

        # Проверяем, что функция выбрасывает исключение
        with pytest.raises(Exception, match="Ошибка запроса 500"):
            get_currency_stocks("dummy_path.json")


# Тест для пустого результата в get_exchange_rate
def test_get_exchange_rate_empty():
    # Мокируем файл с настройками
    mock_settings = '{"user_stocks": ["AAPL"]}'
    with patch("builtins.open", mock_open(read_data=mock_settings)):
        # Мокируем пустой результат yfinance
        with patch("yfinance.Ticker") as mock_ticker:
            mock_ticker.return_value.history.return_value = pd.DataFrame()

            # Вызываем функцию
            result = get_exchange_rate("dummy_path.json")

    # Проверяем результат
    assert len(result) == 0