from BlaBlacarBooking import *
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

    def add_element(self):
        try:
            element = BlablacarBooking()
            element.input()
            self.mas.append(element)
        except ValueError:
            print("Wrong validation!")

    def search_driver(self):
        f = open('Result', 'w')
        for_search = []
        for i in self.mas:
            for j in i.__dict__.values():
                for_search.append(j.DriverName)
        counter = 0
        for k in for_search:
            for i in self.mas:
                for j in i.__dict__.values():
                    if k in j:
                        counter += 1
            element = k + " - " + counter
            element.write()
        f.close()

    def search_hour(self):
        for_search = []
        for i in self.mas:
            for j in i.__dict__.values():
                for_search.append(j.DriverName)
        for k in for_search:
            for i in self.mas:
                for j in i.__dict__.values():
                    if k in j:
                        print(k, " - ", j.Count)

    def read_txt(self, file_name):
        try:
            with open(file_name) as file:
                d, i = {}, 0
                for line in file:
                    try:
                        if line == "\n":
                            i += 1
                            self.mas.append(BlablacarBooking(**d))
                        else:
                            key, value = line.split()
                            d[key[:-1]] = value
                    except ValueError as a:
                        print("Element " + str(i) + " " + str(a))
                        continue
            file.close()
        except FileNotFoundError:
            raise ("File not exit")

    def write_txt(self):
        try:
            f = open("Result", "w")
            f.writelines(str(i) + "\n" for i in self.mas)
            f.close()
        except FileNotFoundError:
            raise ("File not exit")
