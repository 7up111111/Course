# Задание 3.3.
# Пусть номер телефона - это просто семизначное число, а имя - это
# случайная строка символов английского алфавита, имеющая какую-то
# случайную длину от 4 до 10 символов. Сгенерируйте случайную телефонную
# книгу, состоящую из 100000 телефонов и запишите её в файл (убедитесь, что
# у вас действительно 100000 разных телефонов). Придумайте сами в каком
# формате должны храниться данные в этом файле.
# Замечание:
# работа с файлами всегда занимает дольше времени, чем работа с оперативной
# памятью, то есть операции со словарями, списками и т.п. работают в тысячи
# раз быстрее, чем простейшие операции по записи или чтению файлов.

# http://heller.ru/course/viewtopic.php?f=7&t=30

print("Week 3 @ 3.3")

import random
import string

# Эту функцию подсмотрел в интернете
def rand_name(x, y):
    len_name = random.randint(x, y)
    a = string.ascii_letters
    return ''.join([random.choice(a) for b in range(len_name)])

def tel_book(contacts):
    number_from_digit = 7 # кол-во цифр в номере
    number_min_value = 1000000
    number_max_value = 9999999
    name_min_value = 4
    name_max_value = 10
    #print(rand_name(name_min_value, name_max_value))
    #a = [[1, 2], [3, 4]]
    #print(a[0][0])

    #number_from_digit = random.randint(number_min_value, number_max_value)
    #print(number_from_digit)

    # Заполняем телефонную книгу
    list_tel_book_phone = []
    list_tel_book_name = []

    #Заполняем первый элемент
    rand_phone = random.randint(number_min_value, number_max_value)
    list_tel_book_phone.append(rand_phone)
    list_tel_book_name.append(rand_name(name_min_value, name_max_value))
    k = 1
    while k < contacts:
        add_contact = True
        
        rand_phone = random.randint(number_min_value, number_max_value)
        
        for a in range(0, k):
            if list_tel_book_phone[a] == rand_phone:
                add_contact = False
                break
        if add_contact:
            list_tel_book_phone.append(rand_phone)
            list_tel_book_name.append(rand_name(name_min_value, name_max_value))
            k += 1
    #print(list_tel_book_phone)
    #print(list_tel_book_name)

    file = open("3_3.txt", "w")
    for a in range(0, contacts):
        file.write(str(list_tel_book_phone[a]) + "\n")
        file.write(list_tel_book_name[a] + "\n")
    file.close()
    
    return True

print("Start gen")

tel_book(5)

print("Finish gen")

#input()
