"""
Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора строки
и время создания (time.time)
"""
import time


class Mystr(str):
    """Class Mystr"""

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance


sss = Mystr("Привет мир", "Vasya")
print(sss)
print(sss.name)
print(sss.time)
print(sss.upper())
help(sss)
