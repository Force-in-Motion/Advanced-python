import string
from itertools import permutations


# ========================================== 1 ==========================================================

def gen_reverse_value(a: int or float, b: int or float) -> int or float:
    """
    :param a: Принимает числовое значение
    :param b: Принимает числовое значение
    :return: Возвращает генерацию чисел от А до Б в обратном порядке
    """
    assert isinstance(a, (int or float)), TypeError ('Получен не верный тип данных')

    assert isinstance(b, (int or float)), TypeError ('Получен не верный тип данных')

    for elem in range(a, b, -1):
        yield elem

# ========================================== 2 ==========================================================

def gen_fibo_nums() -> int:
    """
    :return: Возвращает бесконечную последовательность чисел фибоначи
    """
    a = 0
    b = 1

    while True:
        a, b = b, a + b
        if b % 5 == 0:
            yield b

# ========================================== 3 ==========================================================

def gen_factorial() :
    """
    :return: Возвращает бесконечную последовательность факториалов чисел
    """
    n = 1
    fact = 1

    while True:
        yield fact
        n += 1
        fact *= n

# ========================================== 4 ==========================================================

def gen_letters() -> str:
    """
    :return: Возвращает бесконечную последовательность букв алфавита
    """
    while True:
        for let in string.ascii_uppercase:
            yield let

# ========================================== 5 ==========================================================

def gen_unique_str(data: str) -> str:
    """
    :param data: Принимает текст
    :return: Возвращает только уникальные слова полученного текста
    """
    assert isinstance(data, str), TypeError ('Получен не верный тип данных')

    for elem in set(data.split(' ' or ',' or '.')):
        yield elem

# ========================================== 6 ==========================================================

def gen_str_by_condition(data: str, k : int) -> str:
    """
    :param data: Принимает текст
    :return: Возвращает слова полученного текста длинна которых, не меньше указанного количества
    """
    assert isinstance(data, str), TypeError ('Получен не верный тип данных')

    assert isinstance(k, int), TypeError ('Получен не верный тип данных')

    lst_str = [i for i in data.split(' ' or ',' or '.') if len(i) >= k]

    lst_str.sort(reverse=True)

    for elem in lst_str:
        yield elem

# ========================================== 7 ==========================================================

def gen_random_str(data: str, n: int) -> str:
    """
    :param data: Принимает строку
    :param n: Принимает количество букв
    :return: Возвращает все возможные варианты подстрок, полученные путем перестановок букв строки согласно заданному количеству
    """
    assert isinstance(data, str), TypeError ('Получен не верный тип данных')

    lst_str = list(''.join(i) for i in set(permutations(data, n)))

    for i in lst_str:
        yield i

# ========================================== 7 ==========================================================

def gen_unique_vowels_letters(data: str) -> str:
    """
    :param data: Принимает текст
    :return: Возвращает все уникальные гласные буквы текста
    """
    assert isinstance(data, str), TypeError ('Получен не верный тип данных')

    lst_str = set([i for i in data if i in 'aeiouAEIOU'])

    for i in lst_str:
        yield i
