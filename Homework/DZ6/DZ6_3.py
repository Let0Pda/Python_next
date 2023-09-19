'''
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.
'''
# Код задачи добавлен в модуль "chess.py" пакета "games" Seminar6
import random


def random_queens():
    return [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]


def queens_safe(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1]:
                return False
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):  # noqa
                return False
    return True


successful = []

while len(successful) < 4:
    queens = random_queens()
    if queens_safe(queens):
        successful.append(queens)
        print(f"Успешная расстановка {len(successful)}: {queens}")
    else:
        print("Неуспешная расстановка")

print("Генерация завершена. 4 успешных расстановки найдены.")

# Вывод всех успешных расстановок после завершения работы
print("Все успешные расстановки:")
for i, arrangement in enumerate(successful, 1):
    print(f"Расстановка {i}: {arrangement}")
