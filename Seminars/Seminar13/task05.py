"""
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4) вход в систему - требует указать имя и id пользователя.
Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа.
А если пользователь есть, получите его уровень из множества пользователей.
Добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
"""
from task03 import LevelException, AccessException
import json


class User:
    def __init__(self, user_name, level, user_id) -> None:
        self.name = user_name
        self.level = level
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"\nUser {self.name} {self.level} {self.user_id}"


def my_json(res):
    with open(res, "r", encoding="utf=8") as f:
        my_dict = json.load(f)
    user_set = set()
    for level, value in my_dict.items():
        for user_id, user_name in value.items():
            new_user = User(user_name, level, user_id)
            user_set.add(new_user)
    return user_set


res = "./Seminars/Seminar13/task04/task04.json"
print(my_json(res))
