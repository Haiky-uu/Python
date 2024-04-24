# 50 get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to find list of non adjacent
# numbers of every number.

a = [2,3,4,55,33,4,55,343,66,77,88,99]

for num in range(len(a)):
    temp = a[num]
    list = []
    if(num>0):
        list.append(a[num-1])
    if(num<len(a)-1):
        list.append(a[num+1])
    print(f"number {temp} non adjacent numbers are {list}")