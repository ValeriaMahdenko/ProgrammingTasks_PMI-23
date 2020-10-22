from datetime import time
class Time():
    def __init__(self, hour, minutes):
       self.hour = hour
       self.minutes = minutes

    def __str__(self):
        time = ""
        time += self.hour + ":" + self.minutes
        return time

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = value

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        self._minutes = value

    def Count_time(self, e_time):
        first = time(int(self.hour), int(self.minutes))
        later = time(int(e_time.hour), int(e_time.minutes))
        c = first - later
        return int(c.hours)
