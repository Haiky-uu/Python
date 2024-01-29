'''Ask the user to enter their first name. if the length of their first name
is under five characers, ask them to enter their surname and join them together
(without a space) and display the name in upper case. if the length of the first name is
five or more characters, display their first name in lower case'''
fName = input("Enter your first name: ")

if (len(fName) < 5):
    sName = input("Enter your surname: ")
    fuName = fName + sName
    print("Your full name is: ",fuName.upper())
else:
    print("You first name is",fName.lower())
