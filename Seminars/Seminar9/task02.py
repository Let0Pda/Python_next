'''
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
'''
from random import randint as rnd


def my_fun(func):
    def wrapper(enigma, num_try):
        if not 1 <= enigma <= 100:
            enigma = rnd(1, 100)
        if not 1 <= num_try <= 10:
            num_try = rnd(1, 10)
        print(enigma, num_try)
        return func(enigma, num_try)
    return wrapper


@my_fun
def new_fun(enigma: int, num_try: int):
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
    new_fun(30, 17)
