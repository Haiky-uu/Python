
# Functions and Recursion
"""
'''Functions
 BLock of statements that perform a specific task
def func_name(param 1,param 2..):
    #Some work
    return val
func_name(arg1,arg2..) # function call
a = 2
b = 5
sum = a+b
print(sum)

# Some code

a = 10
b = 6
sum = a+ b
print(sum)
'''
# Some code
''' You can see in the following above code there is repetition of code 2 times or redundant/duplicate code is there
 To solve that functions are used like this'''
'''

def sum(a,b):  # Defination of function
    sum=a+b
    return sum
print(sum(2,3))  # function call and print the return o/p of function what function has retuns to us
print(sum(10,6))

def new_sum(a,b):
    sum = a+b
    print(sum)
    #return sum
new_sum(8,8)  # this will give print output as print is used in function
print(new_sum(2,3))  # this will give none as no value is returned no return statement is used in function
print(new_sum(4,5))

# Function definition
def calc_sum(a,b):  # Parameters
    return a+b

print(calc_sum(2,3))    # Function call/arguments
# OR storing function o/p in a variable and then print
sum = calc_sum(223,3482) # function call/ arguments
print(sum)

'''
''' Here we have used function to take 2 variables and add them in function and give output
we can call function any time and any number of times'''

'''
def print_hello():
    print('Hello')
print_hello()
print_hello()
print_hello()

def hello_print():
    print("Hellow")
out = hello_print()
print(out) # None
#print(hello_print())
'''
'''

def he():
    print("hello")
    return 'he'
print(he())

'''
''' We can or can't give parameters to function then it will give none if it returns nothing'''

# average of three numbers
'''
def avg_calc(a,b,c):
    sum = a+b+c
    avg = sum/3
    avg = (a+b+c)/3
    return avg
print(avg_calc(2,3,8))
op = avg_calc(4,5,7)
print(op)
'''

'''Types of functions in python
Built_in functions(already build in programming language)  User_defined_functions(that we did above written by us users)
print()
len()
type()
range()'''
# Build in function
print("hello")
# hover over built in functions to know more in pycharm or vs code
# print is function
# hello is an argument

# Default values
''' Assigning a default value to parameter , which is used when no argument is passed
  Default value can be one but it should be passed from the end as first value can be empty'''
'''
def cal_mul(a=1,b=5):
    print(a*b)
cal_mul()
#OR
def cal_mul2(a,b=4): # def cal_mul2(a=3,b) This will not work
    print(a*b)
cal_mul2(3)
'''

# Practice
'''WAF to print the length of a list. (list is the parameter)'''

nums = [1,2,3,4,5,9]
city = ['delhi','gurgaon','mumbai']

def lenlist(list,city):
    print(len(list))
    print(len(city))
lenlist(nums,city)

'''WAF to print the elements of list in a single line. (list is parameter)'''

nums = [1,2,3,4,5,6,7]
def elelist(list):
    for i in list:
        print(i,end=" ")
elelist(nums)

'''WAF to find the factorial of n n is the parameter'''

n = int(input("\nEnter a number:"))

def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    print(fact)
fact(n)

'''WAF to convert USD to INR'''
dollar = int(input("Enter Dolor:"))
def usdc(dl):
    usd=82.89
    rupee = dl*usd
    print(f"{dl} dollor is {rupee} rupee")
usdc(dollar)


'''WAF to check even or odd'''
num = int(input("Enter a number:"))
def even_odd(num):
    if(num%2==0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even_odd(num)

"""

# Recursion
'''When a function calls itself repeatedly 
when function call is written inside a function not outside'''
'''
n = 5
def show(n):
    if(n==0): # this is base case where the recursion stops
        return
    print(n)
    show(n-1)   # Here the function is calling itself
show(10)    # Here the function is called once
'''
''' Call stack :- In programming is a stack where the calling of a recursion is stored
when it calls it self multiple times here stack1 = n=10 stack2 = n=9 unto n=0 stack11 it 
will fill, the layer 11 stack 11 of n = 0 gets deleted as it is returned in if statement.
then all other layers are deleted one by one and o/p is printed and call stack is empty
 functions are given call stacks reserved in programming languages'''

























