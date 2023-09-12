'''
Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого символа
введённой строки отсортированный по убыванию.
'''


def my_str(string):
    string = sorted(set(string), reverse=True)
    new_list = []
    for i in string:
        new_list.append(ord(i))
    return new_list


print(my_str('Hello World'))
