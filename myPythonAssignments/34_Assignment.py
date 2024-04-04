# 34 Get a number from user and check if number is twin prime number

num = int(input("Enter a number:"))
i = 1
count = 0
while (i<=num):
    if(num%i == 0):
        count+=1
    i += 1
i = 1
num += 2
while (i<=num):
    if(num %i ==0):
        count += 1
    i += 1

if (count == 4):
    print("number is a twin Prime number")
else:
    print( "number is not a twin prime")

