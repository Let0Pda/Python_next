'''
Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило:
«число является простым, если делится нацело только на единицу и на себя».
'''


def func_gena(n):
    yield 2
    for i in range(3, n, 2):
        for j in range(2, i):
            if not i % j:
                break
        else:
            yield i


N = 100
print('\nмой вариант выводв')
print(*func_gena(N))
print('\nвариант вывода семинара')
for num in func_gena(N):
    print(num, end=' ')
