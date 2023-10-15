'''
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
'''
# from typing import Callable


def my_fun(enigma: int, num_try: int):
    return my_fun


@my_fun
def new_fun(func):
    for _ in range(num_try):
        my_answer = int(input('Введите число: '))
        if my_answer > enigma:
            print('Меньше')
        elif my_answer < enigma:
            print('Больше')
        else:
            print('Верно')
        break


if __name__ == '__main__':
    my_fun(30, 7)
