# 89 write a program to compute factorial of a number using function

def fact(num: int):

    re = 1
    for i in range(1, num+1):
        re *= i
    return re


num = int(input("Enter a number: "))
print(fact(num))
