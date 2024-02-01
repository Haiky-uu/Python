'''
That is converting one data type of variable to another like int to float or string to int
Type conversion is done automatically by the python interpreter it understands it well
While in type casting we tell python forcefully to convert the variable to another data type
'''

# Type conversion
a = 2
b = 4.25
add = a + b
print(add)
print(type(a), type(b), type(add))
'''It converts automatically to the float as float is superior to int it shows additional info
in form of decimal point as well as it stores larger value than int'''

# Type casting
a = float('2.4')  # or a = float(a)
b = 5
add = a + b
print(add)
print(type(a), type(b), type(add))
'''Here we forced the given string value to convert to float 
we can also print number as a string like
b = str(b)
print(b)
print(type(b))'''

