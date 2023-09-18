'''
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои
загадки.

'''
import task04_quiz


def multi_quiz(my_quit, my_try=3):
    for key, value in my_quit.items():
        print('загадка ', end='')
        task04_quiz.quiz(key, value, my_try)


my_dic = {'ex1': ['ans1', 'ans2', 'ans3'],
          'ex2': ['ans4', 'ans5', 'ans6'],
          'ex3': ['ans7', 'ans8', 'ans9']}
# attempts = 4
multi_quiz(my_dic)
