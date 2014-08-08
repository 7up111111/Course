# Задание 2.2.
# Простым числом называется число, которое не делится ни на какое
# другое число кроме себя самого. Это числа 2, 3, 5, 7, 11, 13, 17
# и так далее (1 простым не считается из соображений удобности).
# Простые числа интересны тем, что любое число может быть представлено
# как произведение простых чисел: 50 = 2*5*5, 70 = 7*2*5. Если числа
# представлены в виде разложения на простые множители, то их очень просто
# делить либо определять, что числа друг на друга не делятся. Так, 70 не
# делится на 50, потому что у 70-ти есть множитель 7, которого нет у 50-ти.
# Зато Очень легко поделить 50 на 2: достаточно вычеркнуть двойку из
# сомножителей: 50/2 = 5*5. Напишите функцию maximum_prime(n), которая
# принимает на вход какое-то натуральное число, а возвращает в качестве
# результата его наибольший простой множитель:
# maximum_prime(70) == 7
# maximum_prime(50) == 5
# maximum_prime(4294967297) = 6700417

# http://heller.ru/course/viewtopic.php?f=7&t=24

print("Week 2 @ 2.2")

# на 32 выдает ошибку
def maximum_prime(n):
    k = 2
    prime_number = int(n / k)
    while n % prime_number != 0:
        print("prime_number = " + str(prime_number) +
              " k = " + str(k))
        k += 1
        prime_number = int(n / k)
        if prime_number <= 2: return n
    return maximum_prime(prime_number)

# Решение photoindra работает правильно но тоже долго,
# немного улучшил скорость mlt = mlt // 2
def maximum_prime2(n):
    mlt = n // 2
    result = n
    while result != 1 and mlt != 1:
        if result % mlt != 0:
            #print("result % mlt != 0 /// result = " + str(result) +
            #      " mlt = " + str(mlt))
            mlt -= 1
        else:
            #print("result % mlt == 0 /// result = " + str(result) +
            #      " mlt = " + str(mlt))
            result = mlt
            mlt = mlt // 2
    return result

# Решение Хеллера

def divide_out(x, divisor):
    """Divide x iteratively on divisor until it can be divided"""
    while x % divisor == 0: x //= divisor
    return x

def maximum_prime3(x):
    """Gets maximum prime divisor"""
    if x == 1: return 1
    x = divide_out(x, 2)
    if x == 1: return 2
    x = divide_out(x, 3)
    if x == 1: return 3
    k = 1
    while True:
        d = 3 * k - 1
        x = divide_out(x, d)
        if x == 1: return d
        d = 3 * k + 1
        x = divide_out(x, d)
        if x == 1: return d
        k += 1

import time

def compare_functions(f, g, arg):
    i = 0
    t1 = 0
    t2 = 0
    while i < 10:
        last_time = time.clock()
        f(arg)
        t1 += time.clock() - last_time
        last_time = time.clock()
        g(arg)
        t2 += time.clock() - last_time
        i += 1
    print("TIME photoindra = " + str(t1) + " TIME heller = " + str(t2))
    return t1 / t2

print("Введите целое число: ")

guess = int(input())

#print("maximum_prime   (" +str(guess) + ") = " + str(maximum_prime(guess)))
#print("maximum_prime 2 (" +str(guess) + ") = " + str(maximum_prime2(guess)))
#print("maximum_prime 3 (" +str(guess) + ") = " + str(maximum_prime3(guess)))
print("compare_functions = " + str(compare_functions(maximum_prime2, maximum_prime3, guess)))

input()
