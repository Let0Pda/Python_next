'''
Создайте пакет с всеми модулями, которые вы создали за время занятия.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции, которые могут
верно работать за пределами модуля.

'''
import games
from games.multi_quiz import my_dic

games.multi_quiz.multi_quiz(my_dic)
