"""
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста и для пользователя.
"""


class Arche:
    """Class Arhive"""

    number = []
    my_str = []

    def __new__(cls, num, my_str):
        instance = super().__new__(cls)
        instance.number.append(num)
        instance.my_str.append(my_str)
        return instance

    def __str__(self) -> str:
        return f"str {self.number = } {self.my_str = }"

    def __repr__(self) -> str:
        return f"repr {self.number } {self.my_str}"


arh1 = Arche(10, "строка")
arh2 = Arche(20, "23568")
arh3 = Arche(30, "строка2")

print(arh3.number, arh3.my_str)
# help(arh1)
print(arh1)
print(repr(arh1))
print(f"{arh1 = }")  # вызов repr
print(f"{arh1}")  # вызов str
