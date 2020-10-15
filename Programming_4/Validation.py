import re
from urllib.request import urlopen


class Validation:
    @staticmethod
    def validate_string( value):
        if any(map(str.isdigit, value)):
            raise ValueError("No integers in string!")
        return value

    @staticmethod
    def validate_number(value):
        try:
            if int(value) < 0:
                raise ValueError("Number must be > 0")
        except ValueError:
            raise ValueError("No letters/characters in number!")
        return value

    @staticmethod
    def validate_nomer( value):
        try:
            if value[0:4] != '+380' or value[0:4] == '+380' and len(value) > 13 or value[0:4] == '+380' and len(value) < 13:
                raise ValueError("Phone number must be format +380XXXXXXXXX")
        except ValueError:
            raise ValueError("Phone number must be format +380XXXXXXXXX")
        return value

    @staticmethod
    def validate_url(value):
        try:
            urlopen(value)
        except ValueError:
            raise ValueError("The website_url is not valid")
        return value

    @staticmethod
    def validate_price(value):
        try:
            x = float(value)
            y = str(x).split('.')
            if len(y[-1]) > 2:
                raise ValueError("Format of budget is wrong!")
        except ValueError:
            raise ValueError("No letters/characters in number!")
        return value

    @staticmethod
    def validate_salary(mounth, year):
        if float(mounth) > float(year):
            raise ValueError("Mouthly budget must be < than yearly!")

    @staticmethod
    def validate_file(filename):
        try:
            file = open(filename)
            return True
        except IOError as e:
            print("File does not exist")
     
