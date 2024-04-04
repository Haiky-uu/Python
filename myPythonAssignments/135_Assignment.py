# Get two dates from config file and generate a
# report that shows last Saturday of every month between these days
import datetime

from conf2 import start_date,end_date
sat =[]
oneDay = datetime.timedelta(days=1)
while start_date < end_date:
    if start_date.weekday()==5:
       # print(start_date)
        sat.append(start_date)
    start_date += oneDay

for d in sat:
    if d.day > 23:
        print(d)