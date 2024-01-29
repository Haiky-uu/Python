
num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

total = num + num2
print(f"Your total of {num} and {num2} is {total}")

while (1):
    another = input("You wan to add another number (y/n): ")
    if (another == 'y'):
        num = int(input("Enter a number: "))
        total = total + num
    else:
        break
print(f"Total is: {total}")

"""
const = int(input("Enter a number: "))

while (1):
    another = int(input("Enter another number: "))
    const += another

    conti = input("Do you want to continue: ")
    if (conti != 'y'):
        break
        
print(const)
"""