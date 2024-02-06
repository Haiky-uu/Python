'''
# Strings:-

str1 = 'This is a string'
str2 = "This is a string"
str3 = """This is a string"""
str4 = "This is a  string. \nand now in new line"  # Using escape sequence charter i.e. \n
str5 = "This is string. \tand now with tab."

# Concatenation
#Joining strings
str1 = 'final'
str2 = 'string'
finalStr = str4 + str5
print(finalStr)
print(str1 +" "+ str2)

# Finding Length of string (in length spaces are also counted)
print(len(finalStr))
print(len(str3))
len1 = len(str1)
print(len1)

# Indexing

str = "New string"
print(str[1])
print(str[4])
s1 = str[3]
print(s1)

# Slicing --Accessing part of a string
# str[starting_idx:ending_idx]

str = "New String"
    #  0123456789
print(str[0:3])
print(str[1:5])
print(str[0:])  # it is str[0:len(str)
print(str[4:len(str)])
print(str[:3])  # it is str[0:6]

# Negative index

str = "Apple"
#   -5-4-3-2-1
print(str[-5:])
print(str[:-1])
print(str[-1])
print(str[-3:-1])
print(str[-5:-2])

# String Functions

str = 'this is python programming language'

print(str)
print(str.endswith('age'))  # returns true if string ends with given substr
print(str.endswith('agu'))
print(str.capitalize())  # capitalizes the first character
print(str.replace('python','c++'))  # replaces all occurrences of given substr
print(str.find('is'))  # returns the first index of the first occurrence of given substr
print(str.find('p'))
print(str.find('c++'))  # returns -1 if given substr doesn't exist found
print(str.count('a'))  # count the occurrence of substr

'''

'''
# Conditional Statements

age = 17

if(age >= 18):
    print("you can vote")
    print("You can drive")

if(True):
    print("This is always true")

light = 'yellow'
if (light == 'red'):
    print('stop')
elif (light == 'green'):
    print('go')
elif (light == 'yellow'):
    print('watch')
else:
    print('wrong input')
print('End of code')
# Note elif is only checked if if condition is false and
# else is executed after all conditions are false if's and elif's ...

# Nesting (Nested if-else)

age =34
if (age > 19):
    if (age >= 80):
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")

# Wap to check if a number entered by user is odd or even
num = int(input("Enter a number: "))
if(num%2==0):
    print("Number is even:",num)
else:
    print("Number is odd:",num)

# Wap to find greatest of 3 numbers entered by user

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 > num2):
    print("number 1 is greater")
elif (num2 > num3):
    print("num 2 is greater")
else:
    print("Num 3 is greater")


# Wap to check if a number is a multiple of 7 or not.

x = int(input("Enter number: "))

if ( x % 7 == 0):
    print(f"Number {x} is multiple of 7")
else:
    print(f"Number {x} is not multiple of 7")
'''



