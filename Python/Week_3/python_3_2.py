# Задание 3.2.
# Найдите описание решета Эратосфена и реализуйте этот алгоритм. Вы должны 
# написать функцию sieve(n), которая возвращает список всех простых чисел 
# вплоть до n. (Если бы функцию maximum_prime из прошлой недели пришлось бы 
# звать для целого набора чисел, то было бы куда эффективнее вначале получить 
# список всех простых чисел используя решето Эратосфена, а затем уже искать 
# делители среди известных простых чисел). Обратите внимание, что в Википедии 
# приведена реализация на Питоне якобы решета Эратосфена. На самом деле 
# приведённый там код - это не решето Эратосфена, а его подобие, которое
# работает на порядок хуже оригинального алгоритма. (Задание со звёздочкой - 
# объясните чем хуже алгоритм из Википедии).

# http://heller.ru/course/viewtopic.php?f=7&t=30

print("Week 3 @ 3.2")

def sieve(n):
    if n <= 1: return False
    prime_numbers = [2]
    if n == 2: return prime_numbers
    if n == 3:
        prime_numbers.append(n)
        return prime_numbers
    sequence_ended = False # Последовательность завершилась
    
    list_n = [] # Список чисел от 0 до n
    i = 0
    while i <= n:
        list_n.append(i)
        i += 1
    
    p = 2
    while not sequence_ended:
        k = 2
        while k * p <= n:
            list_n[k*p] = 0
            k += 1
        if p * 2 <= n:
            for a in range(p + 1, n):
                if list_n[a] != 0:
                    p = a
                    break
        else:
            sequence_ended = True
    for a in range(3, n):
        if list_n[a] != 0:
            prime_numbers.append(a)
    return prime_numbers

print("Введите число: ")

guess = int(input())

print("sieve(" + str(guess) + ") = " + str(sieve(guess)))

input()
