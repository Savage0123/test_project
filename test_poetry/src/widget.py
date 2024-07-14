from test_poetry.src.masks import get_mask_account, get_mask_card_number


def masked_account_card(card_or_account: str) -> str:
    """Функция принимает на вход номер карты/счета и возвращает их маску"""
    if card_or_account[:4] == "Счет":
        return f"{card_or_account[:5]}{get_mask_account(card_or_account[5:])}"
    return f"{get_mask_card_number(card_or_account)}"


def get_data(date: str) -> str:
    """Функция преобразования даты из формата ГГГГ-ММ-ДД в ДД-ММ-ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

# print(masked_account_card("2222 3333 4444 5555"))
