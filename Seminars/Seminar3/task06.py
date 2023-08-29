'''
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
Строки нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного слова был
один пробел между ним и номером строки.
'''


def main() -> None:
    text = input("Введите строку текста: ")
    words = text.split()
    words.sort(key=lambda x: (x, -ord(x[0])))

    max_word_length = max(len(word) for word in words)

    for line_number, word in enumerate(words, start=1):
        print(f"{line_number:>{max_word_length + 2}} {word}")


main()
