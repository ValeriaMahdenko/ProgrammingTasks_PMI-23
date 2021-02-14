import re

class Validation_Time():
    @staticmethod
    def isValidTime(value):
        regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
        p = re.compile(regex)
        if value == "":
            raise ValueError('Wrong time format')
        m = re.search(p, str(value))
        if m is None:
            raise ValueError('Wrong time format')
        else:
            return value