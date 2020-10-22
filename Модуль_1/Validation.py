import re
from Time import Time

class Validation:
    @staticmethod
    def validate_number(value):
        try:
            if int(value) < 1 or int(value) > 5:
                raise ValueError("Number must be > 0")
        except ValueError:
            raise ValueError("No letters/characters in number / Number must be > 0")
        return value

    @staticmethod
    def validate_string(value):
        if any(map(str.isdigit, value)):
            raise ValueError("No integers in string!")
        return value

    @staticmethod
    def time_decorator(func):
        def validate_time(self, time):
            try:
                hour, minutes = time.split(":")
                time = Time(hour, minutes)
            except ValueError:
                raise ValueError("Wrong time format!")
            return func(self, time)

        return validate_time

    @staticmethod
    def check_end_time(func):
        def time_valid(self, start_time, time):
            if (time.hour() < start_time.hour() and time.minutes() <= start_time.minutes() or time.minutes() < start_time().minutes
                    and time.hour() <= start_time.hour() or time.hour() < start_time.hour()):
                print("Start date is later than end date")
            func(self, time)
        return time_valid