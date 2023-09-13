'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
import os


def split_path(path):
    filename, file_extension = os.path.splitext(path)
    path, filename = os.path.split(filename)
    return path, filename, file_extension


path = r'D:\Program Files\JetBrains\PyCharm Community Edition 2023.2.1\build.txt'  # noqa
print(split_path(path))
