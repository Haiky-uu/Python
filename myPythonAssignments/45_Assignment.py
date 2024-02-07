# 45 Ask user to enter 2 lists of 5 elements each (user should enter
# as comma separated string), generate lists from the strings and
# check if two lists entered by user are same

list1 = input("Enter 5 elements separated using comma: ").strip().split(',')
list2 = input("Enter 5 elements separated by comma: ").strip().split(',')
print(list1," ",list2)
if (list1 == list2):
    print("Lists are same")
else:
    print("Lists are not same")

