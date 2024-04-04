# 40 ask user to enter 10 numbers store them in list and print list, count the number of times 10 is present in the list and print the result

lis = []
ask = 'y'
while ask != 'n':
    user = int(input("Enter elements in list: "))
    lis.append(user)
    ask = input("Do you want to continue entering elements in list(y/n): ")
print(lis)
count = 0
for i in lis:
    if (i == 10):
        count += 1

print("Number of occurrence of number 10 in list is", count)


