"""
Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса,
старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов, которые также являются
свойствами экземпляра.
"""


class Arche:
    number = []
    my_str = []

    def __new__(cls, num, my_str):
        instance = super().__new__(cls)
        instance.number.append(num)
        instance.my_str.append(my_str)
        return instance


arh1 = Arche(10, "строка")
arh2 = Arche(20, "23568")
arh3 = Arche(30, "строка2")

print(arh3.number, arh3.my_str)
