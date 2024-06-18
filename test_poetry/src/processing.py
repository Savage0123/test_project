def filter_by_state(dictionary_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает на вход список словарей и значение для ключа state и возвращает новый список, содержащий
    словари, у которых ключ state содержит переданное в функцию значение"""
    result_list = []

    for item in dictionary_list:
        if item.get("state") == state:
            result_list.append(item)
    return result_list


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

def sort_by_date(date_list: list, ascending = True) -> list:
    """Функция принимает на вход список словарей и возвращает новый список с отсортированными по убыванию даты словари"""
    sorted_list = sorted(date_list, key = lambda x: x["date"], reverse = ascending)
    return sorted_list


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))