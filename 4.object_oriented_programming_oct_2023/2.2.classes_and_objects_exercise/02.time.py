# Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers). The class
# should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59.
# You should also create 3 additional instance methods:
# -	set_time(hours, minutes, seconds) - updates the time with the new values
# -	get_time() - returns "{hh}:{mm}:{ss}"
# -	next_second() - updates the time with one second (use the class attributes for validation) and returns the new time
# (use the get_time() method)
#
# Test code1:
# time = Time(9, 30, 59)
# print(time.next_second())
#
# Output1:
# 09:31:00
#
# Test code2:
# time = Time(10, 59, 59)
# print(time.next_second())
#
# Test code3:
# time = Time(23, 59, 59)
# print(time.next_second())
#
# Output3:
# 00:00:00


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.seconds > Time.max_seconds:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes > Time.max_minutes:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        if self.hours > Time.max_hours:
            self.hours = self.hours % 24
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
