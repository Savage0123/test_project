from test_poetry.src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(number):
    assert get_mask_card_number("2222 3333 4444 5555") == number


def test_get_mask_account(account):
    assert get_mask_account("2222 3333 4444 5555") == account
