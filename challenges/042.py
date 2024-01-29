#!/bin/python3

total = 0

for i in range(5):
    num = int(input("Enter 5 numbers: "))
    que = input("You want it included: ")
    if (que == 'y'):
        total = total + num
    print("Your number satus is:",total)
print(total)
