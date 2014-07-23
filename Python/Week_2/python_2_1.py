# Задание 2.1.
# Напишите функцию input_int(a, b), которая будет работать так
# же как функция input() без параметров, но только она будет
# проверять, что введённая пользователем строка действительно
# является числом в интервале [a;b], и если это не так, то будет
# просить пользователя повторить попытку ввода.

# http://heller.ru/course/viewtopic.php?f=7&t=24

print("Week 2 @ 2.1")

def input_int(a, b):

    tracker = 0

    while not tracker:
        print("Введите число от " + str(a) + " до " + str(b))
        guess = input()
        if guess.isdigit() and a <= int(guess) <= b:
            print("Вы правильное число!")
            tracker = 1
        
min_value = 1
max_value = 9

input_int(min_value, max_value);

input()
