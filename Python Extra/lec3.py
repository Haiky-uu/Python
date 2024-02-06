'''
# # List and Tuples # #

# Lists in python --- [] -- we use square brackets in list
""" It is a built-in data type that stores set of values
It can store elements of different types (integer, float, string, etc.)
"""

marks1 = 94.4
marks2 = 87.5
marks3 = 95.2
marks4 = 10.5
marks5 = 55.6
# We do this mostly when having data in diff variables rather use this
marks = [94.4, 87.5, 95.2, 10.5, 55.6]
#Indexes- 0     1     2     3     4
# This is list we store all data in one variable and access it accordingly

print(marks)  # Printing whole list
print(type(marks))  # See type of list
print(len(marks))  # Printing length of list i.e. all_indexes+1 = 5

# Accessing individual elements from list
print(marks[1])
print(marks[0])
print(marks[4])

# We also can store different data types in list int, float, string, character etc unlike array
# And also access them as needed
student = ['Nishad', 80, 7.4, 44, 'A']
print(student)
print(student[0])
student[0] = 'NewStud'
print(student)
# Strings are immutable(cannot change)  while lists are mutable (can change) like change specific value of a index
# We can access, change, delete a specific value

# List Slicing
# Similar to slicing of strings
marks = [87, 22, 54, 67, 21]
# index- 0    1   2   3   4
#        -5  -4  -3  -2  -1 Negative indexes
print(marks[1:])  # Similar to [1:len(marks)]
print(marks[:3])  # Similar to [0:3]
print(marks[1:3])
print(marks[-3:-1])

# List Methods

list = [2, 1, 3, 8]
print(list)
print(list.append(4))
# Here it will print none as there is nothing to return for it
# It will only add 4 to end of list
#  Unlike sting where we can directly print methods here we cannot (see string functions)
list.append(6)  # adds one element at the end of list
# so we write it like this and then print list again
print(list)
list.sort()  # sorting list in ascending order = 0,1,2,3
print(list)
list.sort(reverse=True)  # sorting list in descending order = 3,1,2,0
print(list)
list.insert(1,22)  # insert element at given index and other elements are shifted further
print(list)
list = [2, 1, 3, 1]
list.remove(1)  # Remove first occurrence of element i.e. first 1
print(list)
list.pop(2)  # Removing element by given index
print(list)
'''

'''
# Tuples in Python --- we use () circular brackets in tuples
# A built-in data type that lets us create immutable(cannot change) sequence of values

tup = (1,2,3)
tup = (1,2,3,)  # We can also write tuple like this
print(tup)
print(type(tup))
tup = (1,)  # this is also a valid tuple
print(type(tup))
tup = (1)   # this is not a valid tuple it will be a integer
print(type(tup))
tup = (1,2,3,1,4,1)
print(len(tup))
print(tup[0])  # can print specific values
# tup[0] == 2  # cannot change values or add delete etc..
# Tuple slicing
print(tup[1:3])  # Can do slicing similar to string and list slicing
# Tuple methods
print(tup.index(3))  # prints index of given value
print(tup.count(1))  # prints number of occurrence of given value
'''
'''
# Wap to ask user to enter names of their 3 favorite movies and store them in a list
movieNames= input("Enter 3 movie names with comma:").strip().split(',')
print(movieNames)
'''
'''
# Wap to check if a list contains a palindrome of elements
list = [1, 2, 3, 2, 3]
list = [1, 'abc', 'abc', 1]
list2 = list.copy()
print(list2)
list.reverse()
print(list)
if (list2 == list):
    print("is palindrome")
else:
    print('is not palindrome')
'''

''''
print("Checking list is palindrome or not")
list = input("Enter values with comma: ").strip().split(',')
list2 =[]
for i in range(len(list)-1,-1,-1):
    #print(list[i],end="")
    list2.append(list[i])
#print("list2 is",list2)
if (list == list2):
    print(list,"given list is palindrome")
else:
    print(list,"given is not palindrome")
'''