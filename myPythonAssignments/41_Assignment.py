# 41 start with hard coded list say a = [12,3,34,45,88,23,45,63,3,4,69,99], get two numbers from user, store them in second list. Write a program to check if sencond list is subset of first list. Print the output

a = [12, 3, 34, 45, 88, 23, 45, 63, 3, 4, 69, 99]
b = []
while(len(b)<2):
    user = int(input("Enter 2 numbers: "))
    b.append(user)

flag = True
for i in b:
    if i not in a:
        flag = False
        break

if (flag == True):
    print(f"{b} is subset of {a}")
else:
    print(f"{b} is not subset of {a}")

