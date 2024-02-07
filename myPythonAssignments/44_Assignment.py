# 44 ask user to enter a string and check if the string is a palindrome

user = input("Enter a string: ")
string = ''

for i in range(len(user)-1, -1, -1):
    string = string + user[i]


print(string)

if (user == string):
    print('Is Palindrome')
else:
    print("Is not palindrome")