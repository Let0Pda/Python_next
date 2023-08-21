'''
Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

num = int(input("Введите целое число: "))
s = (f"Шестнадцитиричное представление числа {num}: ")
assignment_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}


# Вариаант 1 -> рекурсивный
def decimalToHexadecimal(num):
    if (num <= 0):
        return ''
    remainder = num % 16
    return decimalToHexadecimal(num//16) + assignment_table[remainder]


print(s, decimalToHexadecimal(num))

# Вариант 2 -> использование спецификатора формата
print(s, '{0:x}'.format(num))

# Проверка с помощью функции hex
print(s, hex(num)[2:])
