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
        return f"\nUser: {self.name} {self.level} {self.user_id}"

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self) -> int:
        return hash((self.name, self.user_id))


class ProjectUser:
    def __init__(self, res) -> None:
        self.users = set()
        self.res = res
        self.user = None

    def my_json(self):
        with open(self.res, "r", encoding="utf=8") as f:
            my_dict = json.load(f)

        for level, value in my_dict.items():
            for user_id, user_name in value.items():
                new_user = User(user_name, level, user_id)
                self.users.add(new_user)
        return self.users

    def login_2_sys(self, user_name, user_id):
        local_user = User(user_name, None, user_id)
        if local_user not in self.users:
            raise AccessException
        for user_items in self.users:
            if user_items == local_user:
                self.user = user_items

    def add_user(self, user_name, level, user_id):
        if self.user is not None and self.user.level < level:
            self.users.add(User(user_name, level, user_id))
        else:
            raise LevelException


res = "./Seminars/Seminar13/task04/task04.json"
user_set1 = ProjectUser(res)
user_set1.my_json()
user_set1.login_2_sys("Bob", "21")
user_set1.add_user("Pittte", "2", 10)
print(user_set1.user)
print(user_set1.users)
