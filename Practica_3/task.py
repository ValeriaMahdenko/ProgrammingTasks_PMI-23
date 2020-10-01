from random import randint
from Double_List import *
#Наприклад, -2 5 6 -3 -4 3 -1. k = 2 Результат: -4 3 6 -1 -2 5 -3.


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
    Mylist = Double_List()
    for i in range(n):
        Mylist.append(randint(a, b))
    return Mylist


def input_array(list, n):
    for i in range(n):
        print("array[", i, "]: ", end=' ')
        el = validate("", choice="pos&neg")
        list.append(el)


def right_shift(list):
    step = validate("Enter the shift step: ", choice="no_neg")
    for i in range(step):
        last = list[len(list) - 1]
        for j in range(len(list)-1, 0, -1):
            list[j] = list[j-1]
        list[0] = last


def create_bool(list):
     new_list = Double_List()
     for i in list:
         if i < 0 :
             new_list.append(0)
         elif i >= 0:
             new_list.append(1)
     return new_list


def create_positive(list):
    positive_list = Double_List()
    for i in reversed(list):
        if i >= 0:
            positive_list.append(i)
    return positive_list


def create_negative(list):
    negative_list = Double_List()
    for i in list:
        if i < 0:
            negative_list.append(i)
    if negative_list.is_empty() == False:
        right_shift(negative_list)
    return negative_list


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


def result_array( bool, pos, neg):
    result = Double_List()
    for i in bool:
        if i == 0:
            result.append(neg[0])
            neg.remove(0)
        elif i == 1:
            result.append(pos[0])
            pos.remove(0)

    return result


while True:
    menu()
    response = validate("Your choice: ", choice="for_response")
    if response == 0:
        print("Thank you for attention!")
        break
    size = validate("Enter size of array:", choice="no_neg")
    list = Double_List()
    if response == 1:
        list = random_array(size)
        print("Our sequence: ", list)
    if response == 2:
        input_array(list, size)
        print("Our sequence: ", list)
    bool = create_bool(list)
    positive = create_positive(list)
    negative = create_negative(list)
    result = result_array(bool, positive, negative)
    print("Our result: ", result)
