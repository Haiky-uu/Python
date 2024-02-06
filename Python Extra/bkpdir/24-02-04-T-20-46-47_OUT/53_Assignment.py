# 53 smallest difference between two numbers from two lists (one number from each list). Input l1: [2,4,6,8], l2:[3,10,18,19] .. Output is 1 for this example

a = [11,7,10,4]
list1=a[0]
for i in a:
    if (i<list1):
        list1 = i

print(list1)
b = [10,22,5,8]
list2=a[0]
for i in b:
    if (i<list2):
        list2=i
print(list2)
print("smalles difference is :",list1-list2)




