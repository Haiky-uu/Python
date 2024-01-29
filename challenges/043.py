#!/bin/python3

ans = input("Enter up or down: ")

if (ans == 'up'):
    num = int(input("Enter a top number: "))

    for i in range(1,num+1):
        print(i)

elif (ans == 'down'):
    num = int(input("Enter a number below 20: "))
    if (num < 20):
        for i in range(20,num-1,-1):
            print(i)
    else:
        print("You havent entered number below 20.")

else:
    print("I don't understand.")
