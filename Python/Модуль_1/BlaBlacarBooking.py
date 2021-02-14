from Validation import Validation
from Validation_Time import Validation_Time
'''
Створити клас BlablacarBooking, який містить такі поля
 1. DriverName (Тільки літери)
 2. NoOfPeople (1-4)
 3. StartTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)).
 4. EndTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)). Min: StartTime.
 5. StartPlace (Тільки літери)
 6. EndPlace (Тільки літери)
'''
el = Validation_Time()
v = Validation()
class BlablacarBooking:
    def __init__(self, DriverName='DriverName', NoOfPeople='NoOfPeople', StartTime='StartTime', EndTime='EndTime',
                  StartPlace='StartPlace', EndPlace='EndPlace'):
        self.DriverName = DriverName
        self.NoOfPeople = NoOfPeople
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.StartPlace = StartPlace
        self.EndPlace= EndPlace
        self.Count = self.Count()

    def __str__(self):
        result = ""
        for i in dir(self):
            if not i.startswith("__") and not i.startswith("_") and i != "input":
                result += i + ": " + str(getattr(self, i)) + "\n"
        return result

    @property
    def DriverName(self):
        return self._name

    @DriverName.setter
    def DriverName(self, value):
        self._name = v.validate_string(value)

    @property
    def NoOfPeople(self):
        return self._people

    @NoOfPeople.setter
    def NoOfPeople(self, value):
        self._people = v.validate_number(value)

    @property
    def StartTime(self):
        return self._starttime

    @StartTime.setter
    @Validation.time_decorator
    def StartTime(self, value):
        self._starttime = el.isValidTime(value)

    @property
    def EndTime(self):
        return self._starttime

    @EndTime.setter
    @Validation.time_decorator
    def EndTime(self, end_time):
        self._endtime = el.isValidTime(end_time)

    @property
    def StartPlace(self):
        return self._startplace

    @StartPlace.setter
    def StartPlace(self, value):
        self._startplace = v.validate_string(value)

    @property
    def EndPlace(self):
        return self._endplace

    @EndPlace.setter
    def EndPlace(self, value):
        self._endplace = v.validate_string(value)

    def input(self):
        K = dict((i, input(i)) for i in dir(self)
                 if not i.startswith("__") and not i.startswith("_") and i != "input")
        for (key, value) in K.items():
            setattr(self, key, K.get(key, value))
        return K

    def Count(self):
        c = self.StartTime.Count_time(self.EndTime)
        return c