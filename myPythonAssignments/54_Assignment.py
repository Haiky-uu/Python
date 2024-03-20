'''
54 get a large list of numbers a = [32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121],
sort the list and search a user given number in list using binary search technique
'''

a = [32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121]
#a.sort()
#print(a)

for i in range(len(a)):
    min_idx= i
    #print(min_idx)
    #print(i)
    for j in range(i+1,len(a)):
        if(a[min_idx]>a[j]):
            min_idx=j
            #print(min_idx)
           # print(a[min_idx])
        a[i], a[min_idx] = a[min_idx], a[i]

for i in range(len(a)):
    print(a[i],end=",")



