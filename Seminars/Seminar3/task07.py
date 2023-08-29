'''
Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква в строке без использования
метода count и с ним.
Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
символа в строке.
Обратите внимание на порядок ключей. Объясните почему они совпадают или не
совпадают в ваших решениях.
'''
# Без использования метода "count"


def without_count(input_string):
    letter_freq = {}

    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_freq:
                letter_freq[char_lower] += 1
            else:
                letter_freq[char_lower] = 1

    return letter_freq


user_input = input("Введите строку текста: ")
result = without_count(user_input)
print('\nБез использования метода "count"')
# print(type(result))
print(result)

# С использованием метода "count"


def count(input_string):
    letter_freq = {}

    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower not in letter_freq:
                letter_freq[char_lower] = input_string.count(char_lower)

    return letter_freq


# user_input = input("Введите строку текста: ")
result = count(user_input)
print('\nС использованием метода "count"')
# print(type(result))
print(result)

'''
Порядок ключей в словаре в обоих решениях будет совпадать, потому что мы
проходим по строке в том же порядке в обоих случаях. Каждый символ добавляется
в словарь только один раз, и порядок итерации по словарю будет соответствовать
порядку добавления символов.
'''
