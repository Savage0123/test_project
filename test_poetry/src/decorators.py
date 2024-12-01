def log(filename=None):
    def decorate(func):
        def wrapper(*args, **kwargs):
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
    return x + y

print(my_function(1, 2))
