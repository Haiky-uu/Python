 # 136 Read a file containing one date per line and find day
 # (Monday, Tuesday etc) for every date.

import datetime as dt

l = []

with open('./dates.py') as d:
    for line in d:
        a = line.strip()
        d = dt.datetime.strptime(a, "%Y-%m-%d")
        l.append(d)

for dates in l:
    if dates.weekday()==0:
        print("Monday: ",dates)
    if dates.weekday()==1:
        print("Tuesday: ",dates)
    if dates.weekday()==2:
        print("Wednesday: ",dates)
    if dates.weekday()==3:
        print("Thursday: ",dates)
    if dates.weekday()==4:
        print("Friday: ",dates)
    if dates.weekday()==5:
        print("Saturday: ",dates)
    if dates.weekday()==6:
        print("Sunday: ",dates)





# print(l)





