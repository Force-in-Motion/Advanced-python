# ================================================= № 1 =============================================
from decorator import decorator


def count_calls(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter

        counter += 1

        print(f'Функция "greet" была вызвана {counter} раз')

        func(*args, **kwargs)

    return wrapper


@count_calls
def greet(name):
    print(f"Привет, {name}!")

# ============================================== № 2 =================================================

def type_check(*expected_types: type):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for i in args:
                assert isinstance(i, expected_types), TypeError('Получен не верный тип данных')

            for i in kwargs.items():
                assert isinstance(i, expected_types), TypeError('Получен не верный тип данных')

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


# ==================================================== № 3 ===================================================

def validate_range(min_value: (int, float), max_value: (int, float)):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for i in args:
                assert isinstance(i, (int, float)), TypeError('Получен не верный тип данных')

                assert i >= min_value and i <= max_value, ValueError(f'Аргумент "value" имеет значение {i}, что выходит за пределы {[min_value, max_value]}')

            for i in kwargs.items():
                assert isinstance(i, (int, float)), TypeError('Получен не верный тип данных')

                assert i >= min_value and i <= max_value, ValueError(f'Аргумент "value" имеет значение {i}, что выходит за пределы {[min_value, max_value]}')

            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f"Установлено значение: {value}%")


# ================================================== № 4 =======================================================

def uppercase_result(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        if not isinstance(result, str): return result

        return result.upper()

    return wrapper


@uppercase_result
def get_greeting(name):
    return f"Привет, {name}"


@uppercase_result
def add_numbers(a, b):
    return a + b

# ================================================== № 5 =======================================================

def call_limit(max_calls):
    counter = 0

    def decorator(func):

        def wrapper(*args, **kwargs):
            nonlocal counter

            counter += 1

            assert counter <= max_calls, RuntimeError('Превышено максимальное количество вызовов функции')

            func(*args, **kwargs)

        return wrapper

    return decorator


@call_limit(max_calls=3)
def print_message(msg):
    print(msg)

print_message("Первый вызов")
print_message("Второй вызов")
print_message("Третий вызов")
print_message("Четвертый вызов")