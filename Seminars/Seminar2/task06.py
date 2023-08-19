'''
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

# val 0 add a balance and count
balance = 0
count = 0

# always repeat the current balance
while True:
    print("Текущий баланс:", balance)
    total_input = input(
        "Выберите действие: пополнить, снять, выйти\n")
    # add a value - total_input an i this have commands

    # пополнить
    if total_input == "пополнить":
        summ_50 = int(input("Введите сумму кратную 50: "))
        if summ_50 % 50 != 0:
            print("Сумма должна быть кратна 50")
            continue
        balance += summ_50
        count += 1
        if count % 3 == 0:
            balance *= 1.03
        if balance >= 5000000:
            balance *= 0.9
    # снять
    elif total_input == "снять":
        summ_50 = int(input("Введите сумму кратную 50: "))
        if summ_50 % 50 != 0:
            print("Сумма должна быть кратна 50")
            continue
        if summ_50 > balance:
            print("Недостаточно средств")
            continue
        a = summ_50 * 0.015
        if a < 30:
            a = 30
        elif a > 600:
            a = 600
        balance -= summ_50 + a
        count += 1
        if count % 3 == 0:
            balance *= 1.03
        if balance >= 5000000:
            balance *= 0.9
    # выйти
    elif total_input == "выйти":
        print("Текущий баланс:", balance)
        break

    else:
        print("Неверное действие")
