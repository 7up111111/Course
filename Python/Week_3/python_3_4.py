# Задание 3.4.
# Прочитайте вашу телефонную книгу из файла:
# а) В словарь
# б) В список кортежей:

# [(1234567, "RandomName"), (0034625, "Olololo"), ...]

# в) В список кортежей, упорядоченных по номеру телефона (подсказка: используйте метод sort):

# [(0034625, "Olololo"), (1234567, "RandomName"), ...]

# Напишите функцию get_name(phone), которая по номеру телефона возвращает имя.
# Для упорядоченного списка придумайте эффективный метод поиска. Сравните
# скорость поиска в трёх случаях (придумайте сами методику, по которой можно
# сравнить скорость).

# http://heller.ru/course/viewtopic.php?f=7&t=30

print("Week 3 @ 3.4")

def read_dictionaries(file_name):
    list_tel_book = {}
    a = 0
    for line in open(file_name):
        if a == 0:
            line_phone = line.rstrip()
            a = 1
        else:
            line_name = line.rstrip()
            list_tel_book[line_phone] = line_name
            a = 0
    return list_tel_book

def read_list_tuples(file_name):
    list_tel_book = []
    a = 0
    for line in open(file_name):
        if a == 0:
            line_phone = line.rstrip()
            a = 1
        else:
            line_name = line.rstrip()
            list_tel_book.append((line_phone, line_name))
            a = 0
    return list_tel_book

def sort_list_tuples(list_tel_book):
    list_tel_book.sort(key=lambda contacts: contacts[0])
    #print(list_tel_book)
    return list_tel_book

def get_name(phone, file_name):
    number_from_digit = 7 # кол-во цифр в номере

    if len(str(guess)) != number_from_digit:
        print("Введен слишком короткий/длинный номер.")
        return False
    else:
        # Поиск в словере
        list_tel_book = read_dictionaries(file_name)
        if str(phone) in list_tel_book:
            print(str(phone) + " : " + str((list_tel_book[str(phone)])) + " @ read_dictionaries()")
        else:
            print("В телефонной книге нет номера : " + str(phone))

        # Поиск в списке
        list_tel_book = read_list_tuples(file_name)
        if "phone" in list_tel_book:
            print(str(phone) + " : " + str((list_tel_book[str(phone)])) + " @ read_list_tuples()")

        # Поиск в отсортированном списке
    return True

print("Введите 7 значный номер: ")
guess = int(input())

file_name = "3_3.txt"

print("get_name(" + str(guess) + ") = " + str(get_name(guess, file_name)))

#print(read_dictionaries(file_name))
#print(read_list_tuples(file_name))
#print(sort_list_tuples(read_list_tuples(file_name)))
#print(get_name(guess)

input()
