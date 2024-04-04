#128 Ask user to give day, month, year and create date in "YYYY-mm-dd" format

import datetime

import datetime

user = str(input("Enter a date in day/month/year:"))
print(user)
date = user.strip().split('/')
print(date)
date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
print(date)
new_day = date.strftime('%Y,%m,%d')
print(new_day)
