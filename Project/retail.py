#import datetime as dt
#from datetime import timedelta as td
from datetime import(
datetime as dt,
date as date,
timedelta as td
)
import random
idList = []
#import os
#print(os.getcwd())
path = r"./retail.csv"
headerLine = "Date, Member-Visited, Member-id, Store-id, No-of-Products, Product-id\n"
endDate = date.today()
startDate = dt.date(2021,2,6)
#print(endDate,startDate)

for i in range(1,101):
    idList.append(i)


fp = open("./retail.csv",'a')
fp.write(headerLine)
while(startDate!=endDate):
    totalMember = random.randint(15, 40)
    members = random.choices(idList,k=totalMember)

    for member in members:
        storeId = random.randint(1,3)
        totalProduct = random.randint(1,10)
        products = random.choices(idList,k=totalProduct)
        for product in products:
            line = startDate.strftime("%Y-%m-%d")\
               +','+str(totalMember)\
               +","+str(product)\
               +','+str(storeId)\
               +','+str(totalProduct)\
               +','+str(product)+'\n'
            fp.write(line)
    #line = startDate.strftime("%Y-%m-%d") + ","+str(random.randint(15,40))+"\n"

    print(line,end="")
    #fp.write(line)
    startDate += td(days=1)
fp.close()
