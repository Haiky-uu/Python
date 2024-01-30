password = input("Enter a password: ")
passwordAgain = input("Enter a password again: ")

if (password == passwordAgain):
    print("Thank you")
elif (password.lower() == passwordAgain.lower()):
    print("Must be same")
else:
    print("Wrong")