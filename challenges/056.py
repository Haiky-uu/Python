import random

b = random.randint(1,10)
print(b)
def pick(num):
    #print(num)
    a = int(input("Enter a number: "))
    if (num == a):
        print("correct")
    else:
        return pick(b)
pick(b)

'''
number = random.randint(1,10)
print(number)
num = int(input("Enter a number: "))

while(num != number):

    num = int(input("Wrong Number! Keep entering number: "))
    if (num == number):
        print("Correct ")
    else:
        continue
print("Well done")
'''
