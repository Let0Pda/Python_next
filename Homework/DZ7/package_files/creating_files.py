"""
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона
"""

import os
import random
import string


def create_random_files(
    folder_path,
    extension,
    min_name_length=6,
    max_name_length=30,
    min_size=256,
    max_size=4096,
    num_files=42,
):
    if not extension.startswith("."):
        extension = f".{extension}"

    # Создаем папку, если она не существует
    os.makedirs(folder_path, exist_ok=True)

    for _ in range(num_files):
        # Генерируем случайное имя файла
        name_length = random.randint(min_name_length, max_name_length)
        file_name = (
            "".join(random.choice(string.ascii_letters + string.digits) for _ in range(name_length))
            + extension
        )

        # Собираем полный путь к файлу
        file_path = os.path.join(folder_path, file_name)

        # Генерируем случайное количество байт данных
        size = random.randint(min_size, max_size)
        data = os.urandom(size)

        # Создаем файл и записываем в него данные
        with open(file_path, "wb") as file:
            file.write(data)


if __name__ == "__main__":
    folder_path = "./Homework/DZ7/dz7_package/creating_files"
    create_random_files(folder_path, ".txt")
