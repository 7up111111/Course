print("Week 2 @ 2.3")

def fibo_with_recursion(n):
    if n == 0: return 0
    if n == 1: return 1
    else:
        a = fibo_with_recursion(n - 1)
        b = fibo_with_recursion(n - 2)
        result = a + b
        #print("fibo(n - 1) = " + str(a) + " fibo(n - 2) = " + str(b) + " result = " + str(result))
    return result

def fino_without_recursion(n):
    if n == 0: return 0
    if n == 1: return 1
    a = 0 # n - 2
    b = 1 # n - 1
    k = 1
    result = 0
    while k != n:
        #print("k = " + str(k) + " a = " + str(a) + " b = " + str(b) + " result = " + str(result))
        result = a + b
        a = b
        b = result
        k += 1
        #print("*** k = " + str(k) + " a = " + str(a) + " b = " + str(b) + " result = " + str(result))
    return result

import time

def compare_functions(f, g, arg):
    i = 0
    t1 = 0
    t2 = 0
    while i < 1000:
        last_time = time.clock()
        f(arg)
        t1 += time.clock() - last_time
        last_time = time.clock()
        g(arg)
        t2 += time.clock() - last_time
        i += 1
    print("TIME (fibo_with_recursion) = " + str(t1) + " TIME (fibo_without_recursion) = " + str(t2))
    return t1 / t2

print("Введите число: ")

guess = int(input())

print("compare_functions = " + str(compare_functions(fibo_with_recursion, fino_without_recursion, guess)))

input()
