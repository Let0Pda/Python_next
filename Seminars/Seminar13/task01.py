"""
Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
пока он не введёт целое или вещественное число. Обрабатывайте не числовые данные как исключения.
"""


def get(text):
    """
    The function "get" takes a text input and returns a value.

    :param text: The "text" parameter is a string that represents the input text that you want to
    process or analyze
    """
    while True:
        my_text = input(text)
        try:
            num = int(my_text)
            break
        except ValueError:
            try:
                num = float(my_text)
                break
            except ValueError as e:
                print(f"Ваш ввод привёл к ошибке ValueError: {e}\nПопробуйте снова")

    return num


number = get("Введите числовые данные: ")
