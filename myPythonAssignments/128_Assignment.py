#128 Ask user to give day, month, year and create date in "YYYY-mm-dd" format

import datetime

date = input("Enter day month and year: ")
day, month, year = date.split()

date1 = datetime.date(int(year), int(month), int(day))
print(date1)

day = date1.day+12
print(day)


