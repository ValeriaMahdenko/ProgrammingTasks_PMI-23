#Доповнити завдання № 1 з програмування, написавши власні ітератор та генератор для генерації даних для списку завдання.
# Програма повинна мати меню для вибору способу генерації списку з можливістю виходу з меню.
# Розділити програму на декілька файлів, кожен з яких відповідає за свою структурну одиницю.
import random
from Iterator import *
from RandomIterator import *

def options():
    print("1 - Iterator")
    print("2 - Generator")
    print("0 - EXIT")

def gcd_(el, el2):
    while el != 0 and el2 != 0:
        if el > el2:
            el = el % el2
        else:
            el2 = el2 % el
    return el + el2

  
def pair_gcd(mas, n):
    print("Pair:", '\t\t\t', "GCD:")
    i = 0
    for i in Iterator(i, n):
        for j in Iterator(i + 1, n):
            el = mas[i]
            el_2 = mas[j]
            print(el, " and ", el_2, end='\t\t\t')
            print(gcd_(el, el_2))


def generator(n, a, b):
    while n != 0:
        value = randint(a, b)
        n -= 1
        yield value


def mas_with_iterator(n, a, b):
    iterator = Iterator_random(n, a, b)
    mas = []
    for i in iterator:
        mas.append(i)
    return mas


def mas_with_generator(n, a, b):
    mas = []
    for i in generator(n, a, b):
        mas.append(i)
    return mas


def validation(message, choice = " "):
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


def menu():
    while True:
        options()
        response = validation("Your choice: ", choice="for_response")
        if response == 0:
            print("Thank you for attention!")
            break
        n = validation("Enter n: ", choice="no_neg")
        while True:
            try:
                a = validation("Enter the lower limit: ", choice="no_neg")
                b = validation("Enter the upper limit: ", choice="no_neg")
                if a > b:
                    print("Lower limit > Upper limit! Please, try again.")
                    continue
                break
            except ValueError:
                print("Number must be an integer! Please, try again")
                continue
        if response == 1:
            mas = mas_with_iterator(n, a, b)
            print(mas)
            pair_gcd(mas, n)
        if response == 2:
            mas = mas_with_generator(n, a, b)
            print(mas)
            pair_gcd(mas, n)


menu()