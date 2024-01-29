#!/bin/python3

people = int(input("How many people to invite in party: "))

if (people < 10):
    for i in range(1, people+1):
        friend = input("Enter the friends name: ")
        print(friend,"Has been invited.")
else:
    print("Too many friends.")

