print("Week 2 @ 2.3")

def fibo_with_recursion(n):
    if n == 0: return 0
    if n == 1: return 1
    else:
        a = fibo_with_recursion(n - 1)
        b = fibo_with_recursion(n - 2)
        result = a + b
        print("fibo(n - 1) = " + str(a) + " fibo(n - 2) = " + str(b) + " result = " + str(result))
    return result

print("Введите число: ")

guess = int(input())

print("fibo (" +str(guess) + ") = " + str(fibo_with_recursion(guess)))

input()
