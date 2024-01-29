'''Ask a user to enter an integer that is over 500. Work out the square root
of that number and display it to two decimal places'''

from math import sqrt
num = float(input("Enter a number: "))
print("Square root of the number: ",round(sqrt(num),2))
print("",round(num**0.5))