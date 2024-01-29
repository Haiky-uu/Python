import datetime

# Date
d = datetime.date(2018, 7, 4)
print(d)

today = datetime.date.today()
print(today)
print(today.day)
print(today.weekday())  # Monday is 0 Sunday is 6
print(today.isoweekday())  # Monday is 1 Sunday is 7

tdelta = datetime.timedelta(days=7)
print(today + tdelta)  # prints current date + 7 days date you can plus or minus time using time delta

# date2 = date1 + time_delta (we see that above)
# timedelta = date1 + date2 (we see below)

bday = datetime.date(2024, 5,17)
till_bday = bday - today  # This is timedelta
print(till_bday)
print(till_bday.total_seconds())

# Time
t = datetime.time(9, 30, 45, 100000)
print(t.hour)




