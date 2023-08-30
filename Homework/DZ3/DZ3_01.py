'''
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''


def remove_duplicates(input_list):
    result = []
    for item in input_list:
        if input_list.count(item) > 1 and item not in result:
            result.append(item)
    return result


# Пример использования
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8,
              9, 10, 10, 11, 12, 12, 12, 13, 14, 14, 15, 15]
duplicates_list = remove_duplicates(input_list)
print(duplicates_list)
