'''
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''


def print_balance(balance):
    """Выводит текущий баланс на экран."""
    print("Текущий баланс:", balance)


def deposit(balance, count, transaction_history):
    """Пополнение баланса.

    Args:
        balance (float): Текущий баланс.
        count (int): Количество операций.
        transaction_history (list): Список операций.

    Returns:
        tuple: Обновленный баланс, количество операций и история операций.
    """
    summ_50 = int(input("Введите сумму кратную 50: "))
    if summ_50 % 50 != 0:
        print("Сумма должна быть кратна 50")
        return balance, count, transaction_history
    balance += summ_50
    count += 1
    if count % 3 == 0:
        bonus = balance * 0.03
        balance += bonus
        transaction_history.append(("Пополнение", summ_50))
        transaction_history.append(("Бонус", bonus))
    else:
        transaction_history.append(("Пополнение", summ_50))
    return balance, count, transaction_history


def withdraw(balance, count, transaction_history):
    """Снятие средств.

    Args:
        balance (float): Текущий баланс.
        count (int): Количество операций.
        transaction_history (list): Список операций.

    Returns:
        tuple: Обновленный баланс, количество операций и история операций.
    """
    summ_50 = int(input("Введите сумму кратную 50: "))
    if summ_50 % 50 != 0:
        print("Сумма должна быть кратна 50")
        return balance, count, transaction_history
    if summ_50 > balance:
        print("Недостаточно средств")
        return balance, count, transaction_history
    a = summ_50 * 0.015
    if a < 30:
        a = 30
    elif a > 600:
        a = 600
    balance -= summ_50 + a
    count += 1
    transaction_history.append(("Снятие", summ_50))
    transaction_history.append(("Комиссия", a))
    return balance, count, transaction_history


def view_history(transaction_history):
    """Выводит историю операций на экран.

    Args:
        transaction_history (list): Список операций.
    """
    print("История операций:")
    for transaction in transaction_history:
        print(f"{transaction[0]}: {transaction[1]}")


def main():
    global balance, count  # Сделаем balance и count глобальными переменными
    balance = 0
    count = 0
    transaction_history = []  # Список для хранения всех операций

    while True:
        print_balance(balance)
        total_input = input(
            "Выберите действие: пополнить, снять, история, выйти\n")

        if total_input == "пополнить":
            balance, count, transaction_history = deposit(
                balance, count, transaction_history)
        elif total_input == "снять":
            balance, count, transaction_history = withdraw(
                balance, count, transaction_history)
        elif total_input == "история":
            view_history(transaction_history)
        elif total_input == "выйти":
            print("Текущий баланс:", balance)
            break
        else:
            print("Неверное действие")


main()
