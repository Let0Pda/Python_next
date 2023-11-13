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
        """
        The above function is a constructor that initializes the attributes of a user object.

        :param user_name: The user's name. It is a string that represents the name of the user
        :param level: The "level" parameter in the `__init__` method is used to specify the level of the
        user. It could represent the user's skill level, experience level, or any other level that is
        relevant to the context of the program or application
        :param user_id: The user_id parameter is used to uniquely identify a user. It can be a string or
        an integer value that is assigned to each user
        """
        self.name = user_name
        self.level = level
        self.user_id = user_id

    def __repr__(self) -> str:
        """
        The `__repr__` function is used to return a string representation of an object.
        """
        return f"\nUser: {self.name} {self.level} {self.user_id}"

    def __eq__(self, other):
        """
        The `__eq__` function is used to compare two objects for equality.

        :param other: The "other" parameter in the `__eq__` method refers to the object that is being
        compared to the current object for equality
        """
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self) -> int:
        """
        The `__hash__` function is used to compute the hash value of an object.
        """
        return hash((self.name, self.user_id))


class ProjectUser:
    def __init__(self, res) -> None:
        """
        The above function is a constructor that initializes an object with a given parameter.

        :param res: The "res" parameter in the above code is a variable that represents the resolution
        of something. It is used as an input to initialize an object of a class
        """
        self.users = set()
        self.res = res
        self.user = None

    def my_json(self):
        """
        The function "my_json" is a method that is part of a class.
        """
        with open(self.res, "r", encoding="utf=8") as f:
            my_dict = json.load(f)

        for level, value in my_dict.items():
            for user_id, user_name in value.items():
                new_user = User(user_name, level, user_id)
                self.users.add(new_user)
        return self.users

    def login_2_sys(self, user_name, user_id):
        """
        The function "my_json" reads a JSON file, creates User objects based on the data, and adds them
        to a set.
        :return: the set of users that have been added to the "self.users" attribute.
        """
        local_user = User(user_name, None, user_id)
        if local_user not in self.users:
            raise AccessException
        for user_items in self.users:
            if user_items == local_user:
                self.user = user_items

    def add_user(self, user_name, level, user_id):
        """
        The add_user function adds a new user to a system with a given username, level, and user ID.

        :param user_name: The user's name
        :param level: The "level" parameter in the "add_user" method is used to specify the level of the
        user being added. It could be an integer value representing the user's level or a string value
        indicating the user's level. The specific meaning and usage of the "level" parameter would
        depend on the
        :param user_id: The user_id parameter is used to uniquely identify a user. It can be a string or
        an integer value
        """
        if self.user is not None and self.user.level < level:
            self.users.add(User(user_name, level, user_id))
        else:
            raise LevelException


res = "./Seminars/Seminar13/task04/task04.json"
# The line `user_set1 = ProjectUser(res)` is creating an instance of the `ProjectUser` class and
# assigning it to the variable `user_set1`. The `ProjectUser` class represents a project and has
# methods for loading data, logging in users, and adding users. The `res` parameter is the path to a
# JSON file that contains user data.
user_set1 = ProjectUser(res)
user_set1.my_json()
# The line `user_set1.login_2_sys("Bob", "21")` is calling the `login_2_sys` method of the
# `ProjectUser` class. This method is used to log a user into the system by providing their username
# and user ID.
user_set1.login_2_sys("Bob", "21")
# The line `user_set1.add_user("Pittte", "2", 10)` is calling the `add_user` method of the
# `ProjectUser` class. This method is used to add a new user to the system with the given username,
# level, and user ID. In this case, it is adding a user with the name "Pittte", level 2, and user ID
# 10.
user_set1.add_user("Pittte", "2", 10)
# The line `print(user_set1.user)` is printing the value of the `user` attribute of the `user_set1`
# object. This attribute represents the currently logged-in user in the system.
print(user_set1.user)
# The line `print(user_set1.users)` is printing the set of users that have been added to the
# `user_set1` object. This set represents all the users in the system.
print(user_set1.users)
