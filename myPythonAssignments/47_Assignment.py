# 47 Ask user to enter two strings as command line
# arguments and check if 2nd string is subset of 1st
# string without using string functions

str1 = input("Enter a string: ")
str2 = input("Enter second string: ")
list1 = []
list2 = []

flag = True

for i in str2:
    if i not in str1:
        flag = False
if(flag == True):
    print("is subset")
else:
    print("is not subset")

for i in str1:
    list1.append(i)
for j in str2:
    list2.append(j)
flag = True
for i in list2:
    if (i not in list1):
        flag = False

print(list1,list2)

if (flag == True):
    print("is  subset")
else:
    print("is not subset")




