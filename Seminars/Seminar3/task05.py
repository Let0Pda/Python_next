'''
Создайте вручную список с повторяющимися целыми числами.
Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
Нумерация начинается с единицы.
'''
my_list = [1, 1, 1, 1, 2, 2, 2, 4, 4, 5, 7, 45, 45]

new_list = [index for index, value in enumerate(my_list, start=1) if value % 2]
print(new_list)

# Семинар
new_list = []

for index, value in enumerate(my_list, start=1):
    if value % 2:
        new_list.append(index)
print(new_list)
