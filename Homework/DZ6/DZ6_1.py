'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей
даты на проверку.
'''
# исходнный код находится в модуле Seminar6/task07.py

import sys


def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def valid_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 29 if leap_year(year) else 28
    return False if day < 1 or day > max_day else year >= 1 and year <= 9999


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Пожалуйста, передайте дату в формате 'dd.mm.yyyy' как аргумент командной строки, например: (python DZ6_1.py  31.12.2022).")  # noqa
    else:
        date_str = sys.argv[1]
        if valid_date(date_str):
            print(f"{date_str} - Дата существует")
        else:
            print(f"{date_str} - Дата не существует")
