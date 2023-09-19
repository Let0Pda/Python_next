'''
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите
код, решающий задачу о 8 ферзях.
Известно, что на доске 8x8 можно расставить 8 ферзей так, чтобы они не били
друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

'''
# модуль chess.py добавлен в пакет games


def queens_safe(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            # Проверяем, находятся ли ферзи в одной и той же строке или столбце
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1]:
                return False
            # Проверяем, находятся ли ферзи на одной и той же диагонали
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):  # noqa
                return False
    return True


# Пример входных данных: восемь пар координат ферзей
queens = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]

if queens_safe(queens):
    print("Ферзи не бьют друг друга")
else:
    print("Ферзи бьют друг друга")


# # для проверки
# '''
# Генерация  удачных расстановок для проверки работоспособности функции
# 'queens_safe'
# '''


# def is_safe(queens, row, col):
#     return not any(
#         queens[i][1] == col
#         or queens[i][0] + queens[i][1] == row + col
#         or queens[i][0] - queens[i][1] == row - col
#         for i in range(row)
#     )


# def solve_queens(n, queens, row=0):
#     if row == n:
#         return [queens[:]]

#     successful = []
#     for col in range(n):
#         if is_safe(queens, row, col):
#             queens[row] = (row, col)
#             successful.extend(solve_queens(n, queens, row + 1))

#     return successful


# n = 8
# queens = [(0, 0)] * n  # Инициализируем доску 8x8
# generations = 4
# successful = solve_queens(n, queens)
# for i, arrangement in enumerate(successful[:generations]):
#     print(f"Успешная расстановка {i+1}: {arrangement}")

# print(f"Генерация завершена. {generations} успешных найдены.")

# # 1: [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)]
# # 2: [(0, 0), (1, 5), (2, 7), (3, 2), (4, 6), (5, 3), (6, 1), (7, 4)]
# # 3: [(0, 0), (1, 6), (2, 3), (3, 5), (4, 7), (5, 1), (6, 4), (7, 2)]
# # 4: [(0, 0), (1, 6), (2, 4), (3, 7), (4, 1), (5, 3), (6, 5), (7, 2)]
