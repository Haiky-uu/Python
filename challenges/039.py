#!/bin/python

'''Ask the user to enter a number between 1 and 12 and then display the times table for that number'''

num = int(input("Enter a number: "))
count = 0
for i in range(0,10):
    count +=1
    print(num,"*",count,num*count)

