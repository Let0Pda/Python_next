'''
Функция получает на вход список чисел. Отсортируйте его элементы
in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
'''


def my_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                # temp = my_list[j]
                # my_list[j] = my_list[i]
                # my_list[i] = temp
    return my_list


my_list = [1, 7, 9, 5, 4, 6, 3, 8]
print(my_sort(my_list))
