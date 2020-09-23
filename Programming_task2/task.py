import random
# Задано масив цілих чисел розмірності n.
# Здійснити циклічний зсув його від’ємних елементів на k позицій вправо.
# Додатні елементи масиву записати в оберненому порядку.
# Наприклад, -2 5 6 -3 -4 3 -1. k = 2 Результат: -4 3 6 -1 -2 5 -3.

# 5 6 -2 -3 -4 3 -1
# 5 6 -2 -4 3 -3 -1
# -4 5 6 -2 3 -3 -1
# -4 5 6 -1 -2 3 -3
# Після обертання додатніх: -4 3 6 -1 -2 5 -3


def menu():
    print("1 - Random array")
    print("2 - Еnter an array from the keyboard")
    print("0 - EXIT")


def random_array():
    mas = random.sample(range(-100, 100), n)
    return mas


def input_array():
    mas=[]
    for i in range(n):
        while True:
            try:
                print("array[", i, "]: ", end=' ')
                mas.append(int(input()))
            except ValueError:
                print("Number must be an integer! Please, try again.")
                continue
            break
    return mas


def right_shift(mas):
    while True:
        try:
            step = int(input("Enter the shift step: "))
            if step <= 0:
                print("Step must be positive! Please, try again")
                continue
            break
        except ValueError:
            print("Number must be an integer! Please, try again")
            continue
    for i in range(step):
        mas.insert(0, mas.pop())


def create_bool(mas):
     new_mas = []
     for i in range(n):
         if mas[i] < 0 :
             new_mas.append(0)
         elif mas[i] >= 0:
             new_mas.append(1)
     return new_mas


def create_positive(mas):
    positive_mas = []
    for i in range(n):
        if mas[i] >= 0:
            positive_mas.append(mas[i])
    positive_mas.reverse()
    return positive_mas


def create_negative(mas):
    negative_mas = []
    for i in range(n):
        if mas[i] < 0:
            negative_mas.append(mas[i])
    if negative_mas != []:
        right_shift(negative_mas)
    return negative_mas


def validate_size():
    while True:
        try:
            size = int(input("Enter size of array: "))
            if size <= 0:
                print("Size must be positive! Please, try again")
                continue
            break
        except ValueError:
            print("Number must be an integer! Please, try again")
            continue

    return size


def result_array(n, bool, pos, neg):
    result = []
    for i in range(n):
        if bool[i] == 0:
            result.append(negative[0])
            neg.remove(negative[0])
        elif bool[i] == 1:
            result.append(positive[0])
            pos.remove(positive[0])
    return result


while True:
    menu()
    while True:
        try:
            response = int(input("Your choice: "))
            if response >= 3 or response < 0:
                print("The value is incorrect. Please, try again")
                continue
            break
        except ValueError:
            print("Number must be an integer! Please, try again")
            continue
    if response == 0:
        print("Thank you for attention!")
        break
    n = validate_size()
    if response == 1:
        mas = random_array()
        print("Our sequence: ", mas)
    if response == 2:
        mas = input_array()
        print("Our sequence: ", mas)
    bool_mas = create_bool(mas)
    positive = create_positive(mas)
    negative = create_negative(mas)
    result = result_array(n, bool_mas, positive, negative)
    print("Our result: ", result)