#129 Get current date time from system and display units of datetime (year, month, day, hour, minute, second)
import datetime

today = datetime.datetime.now()
print(today)

print("Year: ",today.year)
print("Month: ",today.month)
print("Day: ",today.day)
print("Hours: ",today.hour)
print("Minutes: ",today.minute)
print("Seconds: ",today.second)
print("Micro_Seconds: ",today.microsecond)
