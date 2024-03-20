# Loops In Python
'''
Loops are used to repeat instructions.
'''

"""
# while loop
'''
while True: # Infinite loop
    print("hello")
'''
count = 1  # Iterators which Iterate through loop(or variable which is used to iterate through loop)
# and iteration which is no of iterations in loop here it is 5 and when variable turns 6 loop terminates
while count<=5:  # finite loop until value becomes 6 then terminate loop
    print("Hello",count)
    count += 1      # count will increase by 1 each time loop runs
print("Value of count:", count)

# print 1 to 5
i =1
while i<=5:
    print(i)
    i +=1
print("Loop ended")
# print numbers 5 to 1
i =5
while i>=1:
    print(i)
    i -=1

# below program will cause infinite loop it will never stop
# because condition is not right so always check the logic which you have writen in loop
# infinite loop can cause problem if used in real life projects mostly they are not used
'''
print(" infinite loop problem")
i = 5
while i <= 6:  # check
    print(i)
    i += 1  # check
'''

# Practice While Loop
'''Print numbers from 1 to 100'''
i = 1
while (i<101):
    print(i)
    i+=1
'''Print numbers from 100 to 1'''
i = 100
while(i>0):
    print(i)
    i-=1

'''Print multiplication table of a number n'''
print('table')
i = 1
n = 2
while(i<11):
    print(f"{n}*{i}:",n*i)
    i+=1
'''Print elements of the following list using a loop'''


l = [1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(l):
    print(l[i])
    #i-=1
    i+=1

'''search for a number x in this tuple using loop'''

l = (1,4,9,16,25,36,49,64,81,100)
i = 0
num = int(input("Enter a number:"))
while i<len(l):
    if(num == l[i]):
        print(f"Number found at idx {i} number is {l[i]}")
        break
        # print(l[i])
    i += 1

else:
    print("Number not found")
# Break and continue
'''
Break:- Used to terminate the loop when encountered. 

i = 0
while i<6:
    print(i)
    if(i == 3):
        break
    i+=1
'''

''' 
Continue:- Terminates execution in the current iteration and continues execution of the loop with 
the next iteration

i = 0
while i<=5:
    if (i==3):
        i+=1
        continue
    print(i)
    i+=1

# Printing odd numbers
i = 0
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
'''

"""
# For loops

''' For loops are used for sequence traversal. For traversing list, string, tuples etc.
eg.
1) sequential element traverse through list.
list1 = [2,4,1,5]
for el in list1:
    # some work
    -- Here we are traversing trough list using elements like 2,4,1,5,.. n

2) sequential index traverse trough list.
list = [6,4,3,2]
index-  0,1,2,3

for idx in range(len(list))
    # some work
    -- Here we are traversing through list using index like 0,1,2,3,.. n


list1 = [2,3,4,6]

for el in list1:
    print(el)  # it will print each element in list

for idx in range(len(list1)):
    print(idx)  # it will print index of each element in list
    print(list1[idx])  # it will print each element in list
var = 'mynameisneo'

"""So here we need break because when the if statement gets executed then else will not get executed if 
    i was found if i was not found ten else will get executed and end will get printed
"""
for el in range(len(var)):
    if(var[el]=='i'):
        print('i found')
        break
    print(var[el])
else:
    print("END")

# Lets practice
a = [1,4,9,16,25,36,49,64,81,100]

for el in a:
    print(el)

a = (1,4,9,16,25,36,49,64,81,100)
# Search for number x in list (linear search)
ip = int(input("Enter a element from list:"))
idx = 0
for el in a:

    if (ip == el):
        print("Element Found",el,"at index:",idx)
        break
    idx+=1
    print("Searching for element...",el)
else:
    print("Element not Found",ip)

# range() Function
"""Range Function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default),
and stops before a specified number.
range(start?,stop,step?)"""

print(range(5))

seq =range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

# OR
for i in seq: # or for i in range(5)
    print(i)
el = [1,2,3,4,5]

# range(start)
for el in range(5): # This will print no of element(starting from 0) or index of that element excluding 5
    print(el)   # start = 0 step = 1 stop = 5

# range(start,stop)
for el in range(1,5): # This will print no of elements or index from 1 to 4 excluding 5
    print(el)

# range(start,stop,step)
for el in range(1,5,2): # This will print no of elements by step of 2 mens 1,3 excluding 5
    print(el)

# print all even numbers
for i in range(2,101,2):
    print(i)

# print all odd number
for i in  range(1,102,2):
    print(i)

# print numbers from 1 to 100

for i in range(1,101):
    print(i)

# print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

# print multiplication table of a number n.
n = int(input("Enter a number to print table of:"))

for i in range(1,11):
    print(f"{n}*{i}: {n*i}")


# pass statement
""" Pass is used as a null statement that dose nothing, it is used as a place holder fot future code 
It is not used that much in coding but there is practice use of it for e.g

for el in range(10): # It will give an error like print is expected in for indented block
    #some code
print("hello")

for el in range(10): # This will work as pass is given no error we can use pass in if block and also in try catch
    pass
if (el > 1):
    pass
print("Hello")
"""

# Practice

""" WAP to find the sum of first n natural numbers """

n = int(input("Enter a number:"))
sum = 0
for i in range(1,n+1):
    print(i)
    sum+=i
print("Total Sum=",sum)

"""using while"""

n = int(input("Enter a number:"))
sum = 0
i = 1
while i<=n:
    sum +=i
    print(i)
    i+=1

print("Total Sum:",sum)


""" WAP to find factorial of first n natural numbers """

n = int(input("Enter a number:"))
fact = 1
i = 1
while i<=n:
    sum*=i
    print(i)
    i+=1
print("Factorial of n is",sum)

# Using for loop

n = int(input("Enter a number"))
fact = 1
for i in range(1,n+1):
    print(i)
    sum*=i
print("Factorial of n is:",sum)

'''


