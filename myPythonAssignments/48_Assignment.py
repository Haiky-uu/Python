# 48 start with a hard coded list a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22] and write a program (bubble sort) to sort the list in ascending order - bubble sort

list = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22]

for i in range(len(list)):
    swapped = False
    for j in range(0,len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            swapped = True
    if (swapped == False):
        break
print("sorted array")
for i in range(len(list)):
    print(list[i],end=" ")



