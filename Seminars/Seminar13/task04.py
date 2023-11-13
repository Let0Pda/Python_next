"""
Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
"""

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
