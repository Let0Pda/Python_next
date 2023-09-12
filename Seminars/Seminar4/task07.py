'''
Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''


def calculate_profit(company_data):
    profit_loss = {}
    all_profitable = True

    for company, financials in company_data.items():
        revenue = sum(financials)
        expenses = abs(sum(x for x in financials if x < 0))
        profit = revenue - expenses
        profit_loss[company] = profit

        if profit < 0:
            all_profitable = False

    return profit_loss, all_profitable


# Пример использования функции:
company_data = {
    "Company A": [10000, -2000, 3000],
    "Company B": [-15000, 2000, 4000],
    "Company C": [12000, -3000, -2500],
    "Company D": [2000, -3000, -2500],
}

profits, all_profitable = calculate_profit(company_data)
for company, profit in profits.items():
    print(f"{company}: {profit} прибыль" if profit >=
          0 else f"{company}: {profit} убыток")

print("Все компании прибыльные" if all_profitable else "Есть убыточные компании")  # noqa
