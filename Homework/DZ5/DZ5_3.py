'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''


def fibonacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


n = 10
fib_gen = fibonacci_generator()
for _ in range(n):
    print(next(fib_gen), end=' ')
