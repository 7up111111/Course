print("Week 2 @ 2.2")

def maximum_prime(n):
    k = 2
    prime_number = round(n / k)
    while n % prime_number != 0:
        print(prime_number)
        k += 1
        prime_number = round(n / k)
        if prime_number <= 2: return n
    return maximum_prime(prime_number)

print("Введите целое число: ")

guess = int(input())

print("maximum_prime (" +str(guess) + ") = " + str(maximum_prime(guess)))

input()
