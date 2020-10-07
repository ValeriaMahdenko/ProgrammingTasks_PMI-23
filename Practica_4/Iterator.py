class Iterator:
    #Iterator that counts upward.
    def __init__(self, start=0, finish=0):
        self.start = start
        self.finish = finish

    def __iter__(self):
        return self

    def __next__(self):
        num = self.start
        if self.start >= self.finish:
            raise StopIteration
        else:
            self.start += 1
        return num