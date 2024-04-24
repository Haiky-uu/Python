#"17","get a number from user, write a program to check if number is prime number","17_Assignmentconditional statements","conditional statements","DS and Algorithms 1"

# num = int(input("Enter a number:"))
# i = 2
# count = 0
# while (i<num):
#     if(num%i == 0):
#         count=1
#         break
#     i += 1
# if (count == 1):
#     print(num, " is a Compo")
# else:
#     print(num, " is a prime")

num = int(input("Enter a num:"))
for i in range(2,(num//2)+1):
    if num%i == 0:
        print("is not prime")
        break
else:
    print("prime")