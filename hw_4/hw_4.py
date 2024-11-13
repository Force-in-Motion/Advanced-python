# =========================================== 1 ============================================
import time


class UppercaseFile:
    def __init__(self, path):
        self.__path = path
        self.__content = None
        self.__file = None

    def __enter__(self) -> str:
        """
        Открывает файл, считывает данные, преобразует данные в верхний регистр и возвращает
        :return: Возвращает данные в верхнем регистре
        """
        self.__file = open( self.__path, 'r', encoding='utf-8')

        self.__content = self.__file.read().upper()

        return self.__content

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Закрывает файл после работы с ним
        :param exc_type: Принимает тип исключения
        :param exc_val: Принимает объект исключения
        :param exc_tb: Принимает трейсбэк (полный путь появления исключения )
        :return: None
        """
        self.__file.close()


# =========================================== 2 ============================================

class Timer:
    def __init__(self):
        self.__start_time = None
        self.__result = None

    def __enter__(self) -> object:
        """
        Определяет стартовое время работы блока кода
        :return: Возвращает объект таймера
        """
        self.__start_time = time.time()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Вычисляет время работы блока кода отнимая от текущего времени время старта
        :param exc_type: Принимает тип исключения
        :param exc_val: Принимает объект исключения
        :param exc_tb: Принимает трейсбэк (полный путь появления исключения )
        :return: None
        """
        self.__result = time.time() - self.__start_time
        print(f'Время выполнения: {self.__result}')


# =========================================== 3 ============================================

class SuppressExceptions:
    def __enter__(self) -> object:
        """
        :return: Возвращает объект
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """
        Проверяет тип принимаемого параметра, если не None значит возникло исключение, которое в конечном итоге и выводится на консоль
        :param exc_type: Принимает тип исключения
        :param exc_val: Принимает объект исключения
        :param exc_tb: Принимает трейсбэк (полный путь появления исключения )
        :return: None
        """
        if exc_type is not None:
            print("An error occurred:", exc_value)
        return True

# =========================================== 4 ============================================

class ValidationPassword:
    def __init__(self, input_data):
        self.__password = 'qwer'
        self.__input_data = input_data


    def __enter__(self):
        assert self.__password == self.__input_data, PermissionError("Access denied")


    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
