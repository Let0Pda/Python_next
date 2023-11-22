"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
"""
import logging
from datetime import datetime, date

FORMAT = "%(levelname)-8s %(asctime)s %(message)-4s "
logging.basicConfig(format=FORMAT, level=logging.ERROR)


def date_func(date_text):
    try:
        my_year = datetime.now().year
        number_date, week_day, month = date_text.split()
        number_date = int(number_date[:-2])
        week_day = week_day[:3]
        my_month = month[:3]
        week_day_list_rus = ["пон", "вто", "сре", "чет", "пят", "суб", "вос"]
        month_list = [" ", "янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
        count = 0
        for i in range(1, 32):
            temp = date(my_year, month_list.index(my_month), i)
            if temp.weekday() == week_day_list_rus.index(week_day):
                count += 1
            if count == number_date:
                return temp
        logging.error(f"Ошибка: Неверный формат текста - {date_text}")
        return None
    except ValueError as e:
        logging.error(f"Ошибка: {e}")
        return None


if __name__ == "__main__":
    my_text = "4-й четверг ноября"
    result = date_func(my_text)
    if result:
        print(f"Вычесленная дата текущего года: {result}")
