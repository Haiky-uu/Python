#46 write a function to get maximum element of list and
# second highest element in a list

list = [0,1,2,5,4,8,6,9]
maxn = 0
maxnn = 0
for i in list:
    if (i > maxn):
        maxnn = maxn
        maxn = i
    elif (i > maxnn):
        maxnn = i



print("Max number is: ", maxn)
print("Secod max nuber is: ", maxnn)

