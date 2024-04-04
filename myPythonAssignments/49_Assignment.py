# 49 start with a hard coded list a = [3,4,5,86,34,2,3,4,7,33,44,66,88,34,32,11,22] and write a program (bubble sort) to sort the list in descending order - bubble sort
a = [3, 4, 5, 86, 34, 2, 3, 4, 7, 33, 44, 66, 88, 34, 32, 11, 22]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
for i in range(len(a)):
    print(a[i])