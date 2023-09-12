'''
Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет символ из Unicode,
а значением - целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем
чисел до наибольшего включительно
'''


# def my_uni(string):
#     my_dict = {}
#     string = sorted((string.split()))
#     for i in range(int(string[0]), int(string[1])+1):
#         my_dict[chr(int(i))] = i
#     return(my_dict)


# print(my_uni('55 22'))

def my_uni(string):
    string = sorted((string.split()))
    return {chr(int(i)): i for i in range(int(string[0]), int(string[1])+1)}


print(my_uni('55 22'))
