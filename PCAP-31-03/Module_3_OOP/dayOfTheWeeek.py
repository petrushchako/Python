class WeekDayError(Exception):
    pass

class Weeker:
    _days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self._days_of_week:
            raise WeekDayError("Invalid day of the week.")
        self._day_index = self._days_of_week.index(day)

    def __str__(self):
        return self._days_of_week[self._day_index]

    def add_days(self, n):
        self._day_index = (self._day_index + n) % 7

    def subtract_days(self, n):
        self._day_index = (self._day_index - n) % 7

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
