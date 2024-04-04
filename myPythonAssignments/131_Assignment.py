# 131 Get Date and find last month first date, last quarter 1st date, last year 1st date

import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


# user = input("Enter date in /: ").strip().split('/')
# print(user)
# ate = datetime.date(int(user[2]),int(user[1]),int(user[0]))
date = datetime.date(2001,4,17)
print(date)

last_m = datetime.date(date.year,date.month-1,1)
print(last_m)

last_q_f = datetime.date(date.year, date.month-3,1)
print(last_q_f)


# last_y = date-relativedelta(years=1)

#month = int(input("Enter a month: "))
last_year = datetime.date(date.year - 1,1,1)
# or last_year = date.replace(date.year-1,month=1,day=1)


print(last_year)

