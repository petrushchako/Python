from datetime import datetime, timedelta

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        time_obj = datetime.strptime(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}", '%H:%M:%S')
        updated_time_obj = time_obj + timedelta(seconds=1)
        self.hours = updated_time_obj.hour
        self.minutes = updated_time_obj.minute
        self.seconds = updated_time_obj.second

    def prev_second(self):
        time_obj = datetime.strptime(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}", '%H:%M:%S')
        updated_time_obj = time_obj - timedelta(seconds=1)
        self.hours = updated_time_obj.hour
        self.minutes = updated_time_obj.minute
        self.seconds = updated_time_obj.second

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
