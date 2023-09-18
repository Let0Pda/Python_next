'''
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои
загадки.

'''

# from games.quiz import quiz
from quiz import quiz


_results_dict = {}


def record_result(quiz_text, attempt_number):
    global _results_dict
    if quiz_text not in _results_dict:
        _results_dict[quiz_text] = []
    if attempt_number is not None:
        _results_dict[quiz_text].append(attempt_number)


def display_results():
    global _results_dict
    sorted_results = list(_results_dict.items())
    for quiz_text, attempt_numbers in sorted_results:
        if attempt_numbers:
            min_attempt = min(attempt_numbers)
            attempts_str = ', '.join(map(str, attempt_numbers))
            print(
                f'Загадка "{quiz_text}" была угадана с {min_attempt}-й попытки\
                    (всего попыток: {attempts_str})')
        else:
            print(f'Загадка "{quiz_text}" не была угадана')


def multi_quiz(my_quit, my_try=3):
    for key, value in my_quit.items():
        print('Загадка ', end='')
        answer = quiz(key, value, my_try)
        count = value.index(answer) + 1 if answer in value else None
        record_result(key, count)


my_dic = {'ex1': ['ans1', 'ans2', 'ans3'],
          'ex2': ['ans4', 'ans5', 'ans6'],
          'ex3': ['ans7', 'ans8', 'ans9']}


if __name__ == '__main__':
    # attempts = 4
    multi_quiz(my_dic)

print("Результаты угадывания:")
display_results()
