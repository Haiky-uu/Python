import random
'''
num = random.randint(1,10)
number = int(input("Enter a number: "))
while(number != num):
    if(number > num):
        print("Too high!")
    else:
        print("Too low")
    number = int(input("Enter again: "))
print("Correct")
'''
'''
num = random.randint(1,10)
print(num)
number = int(input("Enter a number: "))
def rec(num):
    if (number>num):
        print("Too high")
    elif (number<num):
        print("Too low")
    else:
        print("correct")
    return rec(num) 
rec(num)




'''