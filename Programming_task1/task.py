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


try:
    n = int(input("Enter n: "))
    if n < 0:
        print("Number must be positive!")
        exit(0)
    print("Enter the range limits:")
    a = int(input("a: "))
    if a < 0:
        print("Number must be positive!")
        exit(0)
    b = int(input("b: "))
    if b < 0:
        print("Number must be positive!")
        exit(0)
except ValueError:
    print("Number must be an integer!")
    exit(0)

mas = random.sample(range(a, b+1), n)
print("Our sequence: ", mas)
print("Pair:", '\t\t\t', "GCD:")
for i in range(n):
    for j in range(i+1, n):
        a = mas[i]
        b = mas[j]
        print(a, " and ", b, end='\t\t\t')
        print(gcd_(a, b))
