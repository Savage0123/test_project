def log(filename=None):
    """
    Декоратор для логирования выполнения функции.

    Args:
        filename (str, optional): Имя файла для записи логов. Если не указано, логи выводятся в консоль.

    Returns:
        function: Декорированная функция с логированием.
    """
    def decorate(func):
        """
        Внутренняя функция-декоратор.

        Args:
            func (function): Функция, которую нужно декорировать.

        Returns:
            function: Обернутая функция с логированием.
        """
        def wrapper(*args, **kwargs):
            """
            Обертка вокруг декорируемой функции.

            Args:
                *args: Позиционные аргументы функции.
                **kwargs: Именованные аргументы функции.

            Returns:
                Any: Результат выполнения декорируемой функции.
            """
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as mistake:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ошибка: {mistake}. Inputs: ({args}, {kwargs})")
                else:
                    print(f"{func.__name__} ошибка: {mistake}. Inputs: ({args}, {kwargs})")

        return wrapper

    return decorate


@log()
def my_function(x, y):
    """
    Пример функции, которая складывает два числа.

    Args:
        x (int or float): Первое число.
        y (int or float): Второе число.

    Returns:
        int or float: Сумма x и y.
    """
    return x + y


print(my_function(1, 2))