from test_poetry.src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_transaction_descriptions():
    transactions = [
        {"description": "Payment for groceries"},
        {"description": "Transfer to friend"},
        {"description": "Salary"},
    ]
    result = list(transaction_descriptions(transactions))
    assert len(result) == 3
    assert result == ["Payment for groceries", "Transfer to friend", "Salary"]


def test_card_number_generator():
    card_number = card_number_generator(1, 5)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"
