'''
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и
количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль,
если попытки исчерпаны.

'''


def quiz(my_str, my_solve, my_try=3):
    print(my_str)
    count = 0
    while count < my_try:
        answer = input('Введите ответ: ')
        if answer in my_solve:
            print(f'Вы угадали: это {answer}  \nС попытки N {count+1}')

        count += 1
    print('Вы не угадали')
    return answer


if __name__ == '__main__':
    my_quiz = 'Зимой и летом одним цветом'
    my_answer = ['елка',
                 'ель',
                 'сосна']
    attempts = 4

    print(quiz(my_quiz, my_answer, attempts))
