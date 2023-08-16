from random import randint
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10
# попыток. Программа должна подсказывать «больше» или «меньше» после каждой
# попытки. Для генерации случайного числа используйте код:

LOWER_LIMIT = 0
UPPER_LIMIT = 1001

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print('Угадай число от 0 до 1000 за 10 попыток!')

for i in range(1, 11):
    my_num = int(input(f'Попытка № {i}: '))
    if num > my_num:
        print('Больше!')
    elif num < my_num:
        print('Меньше!')
    else:
        print('Угадал!')
        exit()

print('Проиграл!')
