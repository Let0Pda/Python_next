# DZ6_2.py


import random


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

while len(successful) < 4:
    queens = random_queens()
    if queens_safe(queens):
        successful.append(queens)
        print(f"Успешная расстановка {len(successful)}: {queens}")
    else:
        print("Неуспешная расстановка")

print("Генерация завершена. 4 успешных расстановки найдены.")
print("Все успешные расстановки:")
for i, arrangement in enumerate(successful, 1):
    print(f"Расстановка {i}: {arrangement}")
