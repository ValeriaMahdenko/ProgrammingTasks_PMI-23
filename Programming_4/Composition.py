from Department import Department
from operator import attrgetter

import inspect

class Composition:
    def __init__(self):
        self.mas = []

    def add(self, element):
        self.mas.append(element)

    def __setitem__(self, floor_number, data):
        self.mas[floor_number] = data

    def __getitem__(self, key):
        return self.mas[key]

    def __len__(self):
        return len(self.mas)

    def __str__(self):
        x = ""
        for i in self.mas:
            x += str(i) + "\n"
        return x

    def search(self, key):
        for_search = []
        key = key.lower()
        for_search = filter(lambda x: any(key in str(s) for s in x.__dict__.values()), self.mas)
        return for_search

    def delete_by_id(self, iden):
        for i in self.mas:
            if int(i.ID) == int(iden):
                self.mas.remove(i)
            else:
                print("No element in list with ID " + iden)
        return self.mas

    def add_element(self):
        element = Department()
        element.input()
        print(element)
        self.mas.append(element)

    def sort(self, key=" "):
        result = []
        if key == 'director_name':
            result = sorted(self.mas, key=lambda el: getattr(el, key).lower())
        elif key == 'title':
            result = sorted(self.mas, key=lambda el: getattr(el, key).lower())
        else:
            result = sorted(self.mas, key=lambda el: getattr(el, key))
        return result
        #self.mas = sorted(self.mas, key=lambda w: attrgetter(key)(w).lower())
        #self.mas = sorted(self.mas, key=attrgetter(key))

    def edit_by_id(self, iden):
        for i in range(len(self.mas)):
            if int(self.mas[i]._ID) == int(iden):
                new = Department()
                new.input()
                self.mas.insert(i, new)
                self.mas.remove(self.mas[i+1])
            else:
                print("No element in list with ID " + iden)

    def read_txt(self, file_name):
        try:
            with open(file_name) as file:
                d, i = {}, 0
                for line in file:
                    try:
                        if line == "\n":
                            i += 1
                            self.mas.append(Department(**d))
                        else:
                            key, value = line.split()
                            d[key[:-1]] = value
                    except ValueError as a:
                        print("Element " + str(i) + " " + str(a))
                        continue
            file.close()
        except EOFError:
            raise ("File not exit")

    def write_txt(self, file_name):
        try:
            f = open(file_name, "w")
            f.writelines(str(i) + "\n" for i in self.mas)
            f.close()
        except EOFError:
            raise ("File not exit")

