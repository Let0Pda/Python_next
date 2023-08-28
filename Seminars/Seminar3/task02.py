'''
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если
возможно в один из вариантов ниже:
● целое положительное число
● вещественное положительное или отрицательное число
● строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
● строку в верхнем регистре в остальных случаях
'''
'''
user_input = input("Введите данные: ")

# Проверка на целое положительное число
if user_input.isdigit():
    converted_data = int(user_input)
    print("Преобразованное значение:", converted_data,
          "(Целое положительное число)")

# Проверка на вещественное положительное или отрицательное число
elif user_input.replace(".", "", 1).replace("-", "", 1).isdigit():
    converted_data = float(user_input)
    print("Преобразованное значение:", converted_data, "(Вещественное число)")

# Проверка на строку с заглавными буквами
elif any(char.isupper() for char in user_input):
    converted_data = user_input.lower()
    print("Преобразованное значение:", converted_data,
          "(Строка в нижнем регистре с заглавными буквами)")

# Строка в нижнем регистре в остальных случаях
else:
    converted_data = user_input.lower()
    print("Преобразованное значение:", converted_data,
          "(Строка в нижнем регистре)")

'''
a = input('Введите что нить ')
if a.isdigit():
    print(int(a))
elif a.replace(".", "", 1).replace("-", "", 1).isdigit():
    print(float(a))
elif a != a.lower():
    a = a.lower()
else:
    a = a.upper()
print(a)


# a = input('Введите что нибудь ')
if a.isdigit():
    print(int(a))
elif a.replace(".", "", 1).replace("-", "", 1).isdigit():
    print(float(a))
else:
    # if a != a.lower():
    #     a = a.lower()
    # else:
    #     a = a.upper()
    a = a.lower() if a != a.lower() else a.upper()
print(a)
