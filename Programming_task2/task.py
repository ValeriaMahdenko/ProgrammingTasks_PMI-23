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


def random_array(n):
    while True:
        try:
            a = validate("Enter the lower limit: ", choice="pos&neg")
            b = validate("Enter the upper limit: ", choice="pos&neg")
            if a > b:
                print("Lower limit > Upper limit! Please, try again.")
                continue
            break
        except ValueError:
            print("Number must be an integer! Please, try again")
            continue
    mas = random.sample(range(a, b), n)
    return mas


def input_array(mas, n):
    for i in range(n):
        print("array[", i, "]: ", end=' ')
        el = validate("", choice="pos&neg")
        mas.append(el)


def right_shift(mas):
    step = validate("Enter the shift step: ", choice="no_neg")
    for i in range(step):
        mas.insert(0, mas.pop())


def create_bool(mas, n):
     new_mas = []
     for i in range(n):
         if mas[i] < 0 :
             new_mas.append(0)
         elif mas[i] >= 0:
             new_mas.append(1)
     return new_mas


def create_positive(mas, n):
    positive_mas = []
    for i in range(n):
        if mas[i] >= 0:
            positive_mas.append(mas[i])
    positive_mas.reverse()
    return positive_mas


def create_negative(mas, n):
    negative_mas = []
    for i in range(n):
        if mas[i] < 0:
            negative_mas.append(mas[i])
    if negative_mas != []:
        right_shift(negative_mas)
    return negative_mas


def validate(message, choice = " "):
    while True:
        try:
            el = int(input(message))
            if choice == "no_neg":
                if el <= 0:
                    print("Number must be positive! Please, try again")
                    continue
            if choice == "for_response":
                if el >= 3 or el < 0:
                    print("The value is incorrect. Please, try again")
                    continue
            break
        except ValueError:
            print("Number must be an integer! Please, try again")
            continue
    return el


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
    response = validate("Your choice: ", choice="for_response")
    if response == 0:
        print("Thank you for attention!")
        break
    size = validate("Enter size of array:", choice="no_neg")
    arr = []
    if response == 1:
        arr = random_array(size)
        print("Our sequence: ", arr)
    if response == 2:
        input_array(arr, size)
        print("Our sequence: ", arr)

    bool_arr = create_bool(arr, size)
    positive = create_positive(arr, size)
    negative = create_negative(arr, size)
    result = result_array(size, bool_arr, positive, negative)
    print("Our result: ", result)
