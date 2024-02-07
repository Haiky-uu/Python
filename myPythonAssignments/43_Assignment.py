# 43 ask user to enter a string, ask user to enter a character, write a program to check number of occurances of that character in the string given by user.

user = input("Enter a string: ")
print("Sting is: ", user)
a = []
for i in user:
    # print(i)
    a.append(i)

print(a)

user = input("Enter a charater: ")
count = 0
for i in a:
    if (user == i):
        count += 1
print(count)
