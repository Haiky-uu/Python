#!/bin/python3

name = input("Enter a name: ")
num = int(input("Enter a number: "))

if (num < 10):
    for i in range(0,num):
        print(name)
else:
    for i in range(3):
        print("Too High")

