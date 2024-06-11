def masked_account_card(splited_str: Union[list]) -> Union[str]:
    """Функция принимает на вход номер карты/cxtnf и возвращает их маску"""
    masked_number = str()
    for i in splited_str:
        if i.isalpha():
            masked_number += i + " "
        elif i.isdigit() and len(i) == 16:
            masked_number += masked_card_number(i)
        elif i.isdigit() and len(i) == 20:
            masked_number += masked_account_number(i)
    return masked_number


def get_data(date: str) -> str:
    """Функция преобразования даты из формата ГГГГ-ММ-ДД в ДД-ММ-ГГГГ"""
    return (f"{date[8:10]}.{date[5:7]}.{date[0:4]}")


print(get_mask_account_card)
print(get_data)