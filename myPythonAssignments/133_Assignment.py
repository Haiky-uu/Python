# Get endDate from config file, get numdays from config file,
# calculate begin date as endDate - numDays, Find number of saturdays
# between these two dates, exclude 3rd Saturdays that are 3rd Saturday
# of that month. Write date and associated count in a csv file.
# ** NAME this program as "countSaturday.py"
import datetime

from conf2 import end_date,days

startDate = end_date - days
#print(startDate)
#print(end_date)
dates = []
month = []

oneday = datetime.timedelta(days=1)
cnt = 0
while startDate < end_date:

    if startDate.weekday() == 5:
        # print(startDate)
        dates.append(startDate)
    if startDate.month :
        month.append(startDate.month)



    startDate += oneday
a = 0
for d in month:
    a += d
    if a != d:
        print()
#print(dates)
#print(month)

print("No of saturdays: ",cnt)