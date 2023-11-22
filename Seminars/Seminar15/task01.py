"""
Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""
import logging

my_log = "d:/GitTest/Python_next/Seminars/Seminar15/task01.log"
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    filename=my_log,
    encoding="utf8",
    level=logging.ERROR,
    datefmt="%H:%M:%S %d-%m-%Y",
)


def division(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        logging.error(f"Деление на ноль {a=} {b=}")
        res = None
    return res


if __name__ == "__main__":
    print(division(6, 0))
