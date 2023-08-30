'''
Создайте вручную кортеж содержащий элементы разных типов. Получите из него
словарь списков, где ключ - тип элемента, а значение - список элементов
данного типа.
'''


# my_tuple = (1, 'apple', 3.14, 'banan', 42, 2.71, 'mama', True)

# result = {}

# for item in my_tuple:
#     result.setdefault(type(item).__name__, []).append(item)

# print(result)

a_tuple = ('adsd', 'папа', 123, 456, 1.234, True, False)

my_dict = {type(i): [] for i in a_tuple}
for i in a_tuple:
    my_dict[type(i)].append(i)
print(my_dict)

# Семинар
my_dict = {}
# for i in a_tuple:
#     my_dict[type(i)] = list()
# for i in a_tuple:
#     my_dict[type(i)].append(i)
# print(my_dict)

for i in a_tuple:
    if type(i) in my_dict:
        my_dict[type(i)].append(i)
    else:
        my_dict[type(i)] = [i]
print(my_dict)
