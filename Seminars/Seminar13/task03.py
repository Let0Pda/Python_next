"""
Создайте класс с базовым исключением и дочерние классы-исключения:
ошибка уровня,
ошибка доступа.
"""


class MyException(Exception):
    pass


class LevelException(MyException):
    pass


class AccessException(MyException):
    pass
