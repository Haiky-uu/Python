'''Ask for the radius and the depth of a cylinder and work out the total volume
(circle area * depth) rounded to three decimal places'''
import math

radius = float(input("Enter the radius of circle: "))
area = math.pi*(radius**2)
depth = float(input("Enter the depth of the circle: "))
print("Volume of circle: ",area*depth)




