# Get two dates from config file and generate a
# report that shows 1st Monday of every month between these days
import datetime
from dateutil.relativedelta import relativedelta
from conf2 import start_date,end_date
dates = []
#print(start_date)
#print(end_date)
one_day = datetime.timedelta(days=1)
#one_month = datetime.date.rd(months=1)
while start_date < end_date:
    if start_date.weekday() == 0:
       print(start_date)
       # start_date+=relativedelta(months=1)
       start_date = datetime.date(start_date.year,start_date.month+1,1)


    else:
        start_date+=datetime.timedelta(days=1)






