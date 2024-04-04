#24 Ask user to pick any number between 0 and 100 and implement guessing game program to identify number picked by user.
import random

num = random.randint(1,100)
#print(num)
ans = int(input("Enter a number: "))

while(ans != num):

    if(ans > num):
        print("Too high")
    else:
        print("Too low")
    ans = int(input("Enter a number: "))
print("Correct")
