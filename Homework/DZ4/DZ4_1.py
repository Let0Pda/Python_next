'''
Напишите функцию для транспонирования матрицы
'''
import itertools


def transpose_matrix(matrix) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i, j in itertools.product(range(rows), range(cols)):
        transposed[j][i] = matrix[i][j]
    return transposed


# Пример использования функции
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

result = transpose_matrix(matrix)
for row in result:
    print(row)
