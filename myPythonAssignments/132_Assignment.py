# 132 get endDate from config file, get num days from config file, calculate
# begin date as endDate - numDays  and generate a report
# that shows all weekend dates between these days
# (write dates and associated weekday in a csv file)
import datetime

import conf2 as cf

startDate = cf.end_date - cf.days

# print(cf.end_date)
print("S:",startDate)
one_day = datetime.timedelta(days=1)

with open('days.csv','w') as f:

    # wDay = startDate.weekday()
    while startDate < cf.end_date:
        if startDate.weekday() in [0,1,2,3,4]:
            print("Weekday:",startDate)
            f.write("Weekday: "+str(startDate)+'\n')
        if startDate.weekday() in [5,6]:
            print("Weekend: ",startDate)
            f.write("**Weekend: "+str(startDate)+'\n')
        startDate += one_day

f.close()

#print(weekDays)
#print(weekEnds)



