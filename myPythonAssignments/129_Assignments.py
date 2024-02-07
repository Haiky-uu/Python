#129 Get current date time from system and display units of datetime (year, month, day, hour, minute, second)
from datetime import datetime

current_date = datetime.now()
print("Current Date is: ", current_date)

print("Year: ", current_date.year)
print("Month: ", current_date.month)
print("Day: ", current_date.day)
print("Hours: ", current_date.hour)
print("Minutes: ", current_date.minute)
print("Seconds: ", current_date.second)
print("Microseconds: ", current_date.microsecond)


