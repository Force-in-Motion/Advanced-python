# ==================================== 1 =================================================================
from functools import reduce
import math
import random


lst_str = ['22', '49', '89', '9']

list_nums = list(map(lambda x: int(x) if x.isdigit else TypeError('Не верный тип данных'), lst_str))

# ==================================== 2 =================================================================

lst_numbers = [1, 2, 3, 4, 5, 6]

list_even = list(filter(lambda x:  x % 2 == 0, lst_numbers))

# ======================================= 3 ==============================================================

lst_numbers = [1, 2, 3, 4, 5, 6]

result_lst = list(map(lambda x: x**2 if isinstance(x, (int, float))  else TypeError('Не верный тип данных'), lst_numbers))

# ======================================= 4 ==============================================================

lst_str = ["cat", "elephant", "dog", "tiger"]

result_lst = list(filter(lambda x: len(x) > 3, lst_str))

# ======================================= 5 ==============================================================

lst_numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x*y if isinstance(x, (int, float)) and isinstance(y, (int, float)) else TypeError('Не верный тип данных'), lst_numbers)

# ======================================= 6 ==============================================================

lst_str = ["hello", "world", "Python"]

result_lst = list(map(lambda x: len(x) if isinstance(x, str) else TypeError('Не верный тип данных'), lst_str))

# ======================================= 7 ==============================================================

lst_str = ["apple", "banana", "pear", "strawberry"]

result = max(map(lambda x: len(x) if isinstance(x, str) else TypeError('Не верный тип данных'), lst_str))

# ======================================= 8 ==============================================================

lst_str = ["hello", "world"]

result_lst = list(map(lambda x: x.upper() if isinstance(x, str) else TypeError('Не верный тип данных'), lst_str))

# ======================================= 9 ==============================================================

lst_str = ["1", "2", "3", "4"]

result_lst = list(map(lambda x: int(x)**2, list(filter(lambda x: int(x) % 2 == 0 if x.isdigit else TypeError('Не верный тип данных'), lst_str))))

# ======================================= 10 ==============================================================

lst_numbers = [-2, 3, -4, 5, 6]

result = reduce(lambda x, y: x*y, list(filter(lambda x: x >= 0 if isinstance(x, (int, float)) else TypeError('Не верный тип данных'), lst_numbers)))

# ======================================= 11 ==============================================================

lst_str = ["apple", "banana", "orange", "grape"]

result_lst = list(map(lambda x: len(x), list(filter(lambda x: x.startswith(('a', 'e', 'i', 'o', 'u')), lst_str))))

# ======================================= 12 ==============================================================

lst_numbers = [2, 3, 4, 5, 6]

result = reduce(lambda x, y: math.factorial(x) * math.factorial(y), list(filter(lambda x: x % 2 == 0 if isinstance(x, (int, float)) else TypeError('Не верный тип данных'), lst_numbers)))

# ======================================= 13 ==============================================================

lst_str = ["hello", "world", "Python", "is", "great"]

result = ' '.join(list(map(lambda x: x.upper(), list(filter(lambda x: len(x) % 2 == 0, lst_str)))))


# ======================================= Генераторы 1 =====================================================

def multiples_of_five():
    """
    Создает бесконечную последовательность целых чисел, кратных 5.
    """
    num = 0
    while True:
        yield num * 5
        num += 1

# ======================================= Генераторы 2 =====================================================

def multiples_of_number():
    """
    Возвращает квадраты всех целых чисел, начиная с 1.
    """
    num = 0
    while True:
        yield num * num
        num += 1

# ======================================= Генераторы 3 =====================================================

def gen_nums_of_condition(n: int):
    """
    Возвращает числа от 1 до N, но пропускает числа, которые делятся на 3.
    :param n: Принимает число
    """
    num = 0
    while num != n:
        if num % 3 != 0:
            yield num
        num += 1
        continue

# ======================================= Генераторы 4 =====================================================

def gen_words_from_taken_str(data: str, length: int):
    """
    Возвращает все подстроки строки заданной длины.
    :param data: Принимает строку.
    :param length: Принимает длину подстроки.
    :return:
    """
    for i in range(0, len(data) - length + 1, 1):
        yield data[i:i + length]

# ======================================= Генераторы 5 =====================================================

def gen_increases_taken_nums(a: int, b: int):
    """
    Возвращает числа в диапазоне [A, B], каждое увеличенное на 2.
    :param a: Минимальное число
    :param b: Максимальное число
    """
    lst = [i for i in range(a, b, 1)]

    for i in lst:
        yield i + 2

# ======================================= Генераторы 6 =====================================================

def gen_sequence_of_random_nums():
    """
    Возвращает бесконечную последовательность случайных чисел в диапазоне [0, 100].
    """
    while True:
        yield random.randint(0, 100)

# ======================================= Генераторы 7 =====================================================

def gen_fibonachi_nums():
    """
     Возвращает последовательность чисел Фибоначчи.
    """
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

