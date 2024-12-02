class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        total_seconds = self.second + other.second
        total_minutes = self.minute + other.minute + total_seconds // 60
        total_hours = self.hour + other.hour + total_minutes // 60

        return Time(total_hours % 24, total_minutes % 60, total_seconds % 60)

    def display_time(self):
        print(f"{self.hour}h:{self.minute}m:{self.second}s")

# User input
print("Enter time 1:")
time1 = Time(int(input("Hours: ")), int(input("Minutes: ")), int(input("Seconds: ")))

print("Enter time 2:")
time2 = Time(int(input("Hours: ")), int(input("Minutes: ")), int(input("Seconds: ")))

result = time1 + time2
print("Sum of Times:")
result.display_time()
