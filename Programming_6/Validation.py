import re
from urllib.request import urlopen

class Validation:
    @staticmethod
    def decorator_string(func):
        def validate_string(self, value):
            if any(map(str.isdigit, value)):
                raise ValueError("No integers in string!")
            return func(self, value)
        return validate_string

    @staticmethod
    def decorator_number(func):
        def validate_number(self,value):
            try:
                if int(value) < 0:
                    raise ValueError("Number must be > 0")
            except ValueError:
                raise ValueError("No letters/characters in number!")
            return func(self, value)
        return validate_number

    @staticmethod
    def decorator_nomer(func):
        def validate_nomer(self, value):
            try:
                if value[0:4] != '+380' or value[0:4] == '+380' and len(value) > 13 or value[0:4] == '+380' and len(value) < 13:
                    raise ValueError("Phone number must be format +380XXXXXXXXX")
            except ValueError:
                raise ValueError("Phone number must be format +380XXXXXXXXX")
            return func(self, value)
        return validate_nomer

    @staticmethod
    def decorator_url(func):
        def validate_url(self, value):
            try:
                urlopen(value)
            except ValueError:
                raise ValueError("The website_url is not valid")
            return func(self, value)
        return validate_url

    @staticmethod
    def decorator_price(func):
        def validate_price(self, value):
            try:
                x = float(value)
                y = str(x).split('.')
                if len(y[-1]) > 2:
                    raise ValueError("Format of budget is wrong!")
            except ValueError:
                raise ValueError("No letters/characters in number!")
            return func(self, value)
        return validate_price

