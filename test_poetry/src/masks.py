def get_mask_card_number(card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return card[0:7] + "*" * len(card[7:9]) + " " + "*" * len(card[10:14]) + " " + card[-4:]


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return "*" * len(account[13:-4]) + account[-4:]


print(get_mask_account("2222 3333 4444 5555"))
print(get_mask_card_number("2222 3333 4444 5555"))
