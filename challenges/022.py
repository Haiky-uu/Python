'''Ask user to enter their first name and surname in lower
case Change the case to title case and join them togather.
Diaplay finished result'''

fName = input("Enter first name: ")
lName = input("Enter sur name: ")
fuName = (fName + lName).title()
print("Result: ",fuName)