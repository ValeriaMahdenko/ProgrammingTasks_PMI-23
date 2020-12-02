from random import randint

class Iterator_random:
    #Iterator for random numbers
    def __init__(self, count, start, finish):
        self.count = count
        self.start = start
        self.finish = finish
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.value = randint(self.start, self.finish)
            self.count -= 1
            return self.value
        else:
            raise StopIteration

    def __str__(self):
        return "[ " + str(self.value) + " ]"