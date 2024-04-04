#smallest difference between two numbers from two lists
# (one number from each list). Input l1: [2,4,6,8], l2:[3,10,18,19]
#Output is 1 for this example

string1 = input("Enter list1:")
string2 = input("Enter list2:")
list1 = []
list2 = []

for s in range(len(string1)):
    list1.append(int(string1[s]))
    list2.append(int(string2[s]))

print(list1, list2)

min_diff = list1[0]-list2[0]
#print(mindiff)
for num1 in list1:
    for num2 in list2:
        diff=num1-num2
        if (diff < min_diff):
            min_diff = diff
print("Smallest difference between list is: ",min_diff)


