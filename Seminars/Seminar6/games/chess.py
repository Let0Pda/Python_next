import random

# DZ6_2.py


def queens_safe(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1]:
                return False
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):  # noqa
                return False
    return True


'''
if __name__ == '__main__':
    queens = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]

    if queens_safe(queens):
        print("Ферзи не бьют друг друга")
    else:
        print("Ферзи бьют друг друга")
'''

# DZ6_3.py


def random_queens():
    return [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]


successful = []
count = 0
while len(successful) < 4:
    queens = random_queens()
    count += 1
    if queens_safe(queens):
        successful.append(queens)
        print(f"{count} Успешная расстановка {len(successful)}: {queens}")
    else:
        print(f" {count} Неуспешная расстановка")

print("Генерация завершена. 4 успешных расстановки найдены.")
print("Все успешные расстановки:")
for i, arrangement in enumerate(successful, 1):
    print(f"Расстановка {i}: {arrangement}")

# Вывод
''''
...
352610855 Неуспешная расстановка
352610856 Неуспешная расстановка
352610857 Успешная расстановка 4: [(3, 2), (5, 1), (4, 8), (1, 3), (2, 5), (7, 4), (8, 6), (6, 7)] # noqa
Генерация завершена. 4 успешных расстановки найдены.
Все успешные расстановки:
Расстановка 1: [(6, 1), (7, 3), (1, 4), (8, 7), (2, 2), (3, 5), (5, 6), (4, 8)]
Расстановка 2: [(4, 6), (6, 2), (5, 8), (7, 5), (1, 1), (8, 3), (2, 7), (3, 4)]
Расстановка 3: [(5, 7), (6, 2), (4, 1), (3, 4), (1, 5), (8, 3), (7, 6), (2, 8)]
Расстановка 4: [(3, 2), (5, 1), (4, 8), (1, 3), (2, 5), (7, 4), (8, 6), (6, 7)]
'''
# Время выполнения этого кода равно: 8 857 085.368394852 ms , 8 857,09 s, 2,46h
