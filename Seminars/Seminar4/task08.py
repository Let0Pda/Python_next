'''
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''


def remove_s(string):
    # if len(string) > 1 and string[-1] == "s":
    #     return None
    # else:
    #     return string
    return None if len(string) > 1 and string[-1] == "s" else string


a = 'strings'
b = 'test'
c = 'tes'
s = 's'
t = 'st'
print(f'\nДо замены:\n{a = }\n{b = }\n{c = }\n{s = }\n{t = }')

a = remove_s(a)
b = remove_s(b)
c = remove_s(c)
s = remove_s(s)
t = remove_s(t)

print(f'\nПосле замены:\n{a = }\n{b = }\n{c = }\n{s = }\n{t = }')
