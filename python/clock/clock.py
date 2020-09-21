class Clock:
    def __init__(self, hour, minute):
        self.minute = divmod(minute, 60)[1]
        self.hour = divmod(hour + divmod(minute, 60)[0], 24)[1]

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return self.__repr__() == other

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return self.__add__(-minutes)
