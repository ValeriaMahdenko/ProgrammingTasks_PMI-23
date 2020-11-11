def gcd_(el, el2):
    while el != 0 and el2 != 0:
        if el > el2:
            el = el % el2
        else:
            el2 = el2 % el
    return el + el2


def pair_gcd(mas):
    print("Pair:", '\t\t\t', "GCD:")
    i = 0
    n = len(mas)
    for i in range(i, n):
        for j in range(i + 1, n):
            el = mas[i]
            el_2 = mas[j]
            print(el, " and ", el_2, end='\t\t\t')
            print(gcd_(el, el_2))