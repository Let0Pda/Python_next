"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и значение по умолчанию.
При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def my_get(my_dic, my_key, def_value):
    """
    The function `my_get` returns the value associated with `my_key` in `my_dic`, or `def_value` if
    `my_key` is not found.

    :param my_dic: A dictionary that you want to retrieve a value from
    :param my_key: The key you want to retrieve from the dictionary
    :param def_value: The default value to return if the key is not found in the dictionary
    """
    try:
        result = my_dic[my_key]
    except Exception:
        result = def_value
    return result


my_dic = {"1": "Утро", "2": "День", "3": "Вечер"}
def_value = "Tакого ключа в словаре my_dic не существует."

new_key = "1"

print(my_get(my_dic, new_key, def_value))
