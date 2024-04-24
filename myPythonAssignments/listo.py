# list of list to list

lst = [[2,3],[4,5],[6,7]]
ls = []

price = [(123,22),(1666,11),(3423,3),(7567,10)]

for i in price:
   # print(i[0],i[1])
    a = i[0]
    b = i[1]
    #print(a,b)
    gst = i[0]*(i[1]/100)
    gst += a
    ls.append([a,b,gst])
#print(ls)


for val,gst in price:
    #print(val,gst)
    amt = val*(gst/100)
    amt += val
    ls.append([val,gst,amt])

#print(ls)






