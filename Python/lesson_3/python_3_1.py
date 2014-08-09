# Задание 3.1.
# Если x - строка, то используя x.isdigit() вы можете проверить содержит ли x
# только цифры. Напишите функцию is_number(x), которая будет проверять,
# является ли записанная в x строка произвольным числом:

# is_number("-234.12") == True
# is_number("asdf") == False

# http://heller.ru/course/viewtopic.php?f=7&t=30

print("Week 3 @ 3.1")

def is_number(x):
    """"Проверяем первый симсвол сткроки на - и длину строки > 1 и на число
    Проверяем, что бы в строке была только одна точка или запятая"""
    dot = False
    if (x[0] == "-" and len(x) > 1) or x[0].isdigit():
        for a in x[1:]:
            if (a == "." or a == ",") and not dot:
                dot = True
            elif not a.isdigit(): return False
        return True
    else: return False

print("Введите число: ")

guess = input()

print("is_number(" + str(guess) + ") = " + str(is_number(guess)))

input()
