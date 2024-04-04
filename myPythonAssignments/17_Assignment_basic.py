#"17","get a number from user, write a program to check if number is prime number","17_Assignmentconditional statements","conditional statements","DS and Algorithms 1"
num = int(input("Enter a number:"))
i = 1
count = 0
while (i<=num):
    if(num%i == 0):
        count+=1
    i += 1
if (count == 2):
    print(num, " is a Prime number")
else:
    print(num, " is a composite number")