"""
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке,
от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

    Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
    Декоратор выполняет следующие действия:

Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты
вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация
о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

Пример

На входе:

generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)

На выходе:

True
True

"""
import csv
import random
import math
import json


def generate_csv_file(file_name, rows):
    with open(file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Записываем заголовок, если нужно
        csv_writer.writerow(["Number 1", "Number 2", "Number 3"])

        for _ in range(rows):
            # Генерируем три случайных числа в диапазоне от 100 до 1000
            random_numbers = [random.randint(100, 1000) for _ in range(3)]

            # Записываем сгенерированные числа в файл
            csv_writer.writerow(random_numbers)


def save_to_json(func):
    def wrapper(*args, **kwargs):
        # Чтение данных из CSV-файла
        file_name = args[0]
        data = []
        with open(file_name, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Пропускаем заголовок
            for row in csv_reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data.append({"a": a, "b": b, "c": c, "result": result})

        # Сохранение результатов в JSON-файл
        with open("results.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    # Вычисляем дискриминант
    discriminant = b**2 - 4 * a * c

    # Проверяем значение дискриминанта
    if discriminant < 0:
        return None  # Нет корней
    elif discriminant == 0:
        # Есть один корень
        return -b / (2 * a)
    else:
        # Есть два корня
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)


if __name__ == "__main__":
    generate_csv_file("input_data.csv", 101)
    find_roots("input_data.csv")  # type: ignore

    with open("results.json", "r") as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print("Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 101)
