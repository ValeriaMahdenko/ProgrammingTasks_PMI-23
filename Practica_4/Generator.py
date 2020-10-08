from random import randint


def generator(n, a, b):

    while n != 0:
        value = randint(a, b)
        n -= 1
        yield value
