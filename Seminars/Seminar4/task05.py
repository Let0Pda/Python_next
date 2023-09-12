'''
Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str
с указанием процентов вида “10.25%”.
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
'''


def clear_str(m_list):
    for i in range(len(m_list)):
        m_list[i] = float(m_list[i].replace('%', ""))


def calculate(my_name, my_salary, my_bonus):
    # new_dic = {}
    # for name, salary, bonus in zip(my_name, my_salary, my_bonus):
    #     new_dic[name] = round(salary * (1 + bonus/100), 2)
    # return new_dic
    return {
        name: round(salary * (1 + bonus / 100), 2)
        for name, salary, bonus in zip(my_name, my_salary, my_bonus)
    }


names = ['Сергей', 'Дмитрий', 'Алексей']
salary = [100000, 20000, 30000]
bonus = ['10.25%', '25.30%', '400.45%']

clear_str(bonus)
print(calculate(names, salary, bonus))
