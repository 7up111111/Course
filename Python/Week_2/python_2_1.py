print("Week 2 @ 2.1")

def input_int(a, b):

    tracker = 0

    while not tracker:
        print("Введите число от " + str(a) + " до " + str(b))
        guess = input()
        if guess.isdigit() and a <= int(guess) <= b:
            print("Вы ввели число!")
            tracker = 1
        
        

    #while not guess.isdigit() and a <= int(guess) <= b:
    #    print("Введите число: ")
    #    guess = input()
    
    #while a <= int(guess) <= b:
    #    print("a <= guess <= b")

min_value = 1
max_value = 9

input_int(min_value, max_value);

#input()