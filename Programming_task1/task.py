import random
# Згенерувати послідовність N рандомних чисел з проміжку [a, b].
#  Вивести на екран найбільший спільний дільник для кожної пари цих чисел.


def gcd_(el, el2):
    # Function for finding the GCD( greatest common divisor )
    while el != 0 and el2 != 0:
        if el > el2:
            el = el % el2
        else:
            el2 = el2 % el
    return el + el2


def print_randommas(a, b, n):
    mas = random.sample(range(a, b + 1), n)
    print("Our sequence: ", mas)
    return mas


def pair_gcd(mas, n):
    print("Pair:", '\t\t\t', "GCD:")
    for i in range(n):
        for j in range(i + 1, n):
            el = mas[i]
            el_2 = mas[j]
            print(el, " and ", el_2, end='\t\t\t')
            print(gcd_(el, el_2))


def validation(message):
    while True:
        try:
            el = int(input(message))
            if el < 0:
                print("Number must be positive! Please, try again")
                continue
            break
        except ValueError:
            print("Number must be an integer! Please, try again")
            continue
    return el


n = validation("Enter n: ")
a = validation("Enter a: ")
b = validation("Enter b: ")
arr = print_randommas(a, b, n)
pair_gcd(arr, n)
