import pytest
from test_poetry.src.widget import masked_account_card, get_data


def test_masked_account_card(card):
    assert masked_account_card("2222 3333 4444 5555, 2222 3333 4444 5555") == card


def test_get_data(data):
    assert get_data("2012.12.10") == data
