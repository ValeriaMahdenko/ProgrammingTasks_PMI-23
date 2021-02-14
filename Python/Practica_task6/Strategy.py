from abc import ABC, abstractmethod
from Linked_list import Double_List
from Iterator import Iterator_random
from Validate import *

v = Validate()
class Strategy(ABC):

    @abstractmethod
    def execute(self, *args):
        pass


class Strategy_Iterator(Strategy):
    def execute(self, list: Double_List,  position):
        j = 0
        n = v.valid_positive("Enter n: ")
        a = v.valid_positive("Enter a: ")
        b = v.valid_positive("Enter b: ")
        if a > b:
            print("Lower limit > Upper limit! Please, try again.")
        else:
            iterator = Iterator_random(n, a, b)
            for i in iterator:
                list.insert(i, position)
                position += 1
        return list


class Strategy_File(Strategy):
    def execute(self, list: Double_List, position):
        file_name = input("Enter file name:")
        if v.validate_file(file_name) == True:
            f = open(file_name, 'r')
            counter = 0
            for line in f:
                strs = line.split(' ')
                for s in strs:
                    if s != " ":
                        if int(s) > 0:
                            list.insert(int(s), position)
                            position += 1
                        if int(s) < 0:
                            counter += 1
            if counter > 0:
                print("Element of sequance must be > 0. So, negative elements are not added to the list")
            f.close()
