import random

fname= []
count = 0
fpath = r'firstNames.csv'
lpath = r'lastNames.csv'
for line in open(fpath):
    #print(line)
    if count == 0:
        count+=1
        continue
    srno,firstname,gender=line.strip().split(',')
    fname.append(firstname)
print(fname)

lname=[]
count = 0
for line in open(lpath):
    #print(line)
    if count == 0:
        count+=1
        continue
    #print(line)
    srno,lastname=line.strip().split(',')
    lname.append(lastname)
print(lname)

fullname = []
for i in range(1000):
    first_name = random.choice(fname) # if you do this both choices it will give error
    last_name = random.choice(lname)
    #print(fname+lname)
    #print(first_name + last_name)
    fullname.append(first_name+' '+last_name)
print(fullname)
for line in fullname:
    print(line,end=","+"\n")

''''
first_name=[]
count  = 0
with open('firstNames.csv','r') as first:
    readline = csv.reader(first)
    count+=1
    for line in readline:
        first_name.append(line[1])
print(first_name)

count = 0
last_name=[]
with open('lastNames.csv','r') as last:
    readline = csv.reader(last)
    for line in readline:
        for line in readline:
        last_name.append(line[1])
print(last_name)

fullNames = []

for i in range(1000):
    first = random.choice(first_name)
    last = random.choice(last_name)
    fullNames.append(first+" "+last)
print(fullNames)

'''
