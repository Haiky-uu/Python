'''Ask the user to enter the radious of circle (mesure ment from the center
point to the edge). work out the rea of the circle (pi * radius^2).'''
import math

radius = float(input("Enter a radius of circle: "))
print("Area of circle: ",round(math.pi*(radius**2),4))