'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''

#  Бесконечно генерит числа Фибоначчи при каждом вызове


def fibonacci_gen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


n = 20
fib_gen = fibonacci_gen()
for _ in range(n):
    print(next(fib_gen), end=' ')

print()

# Через условие выхода из цикла 'while'


def fibonacci_gen(limit):
    a, b = 1, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


fib_gena = fibonacci_gen(n)
for number in fib_gena:
    print(number, end=' ')
