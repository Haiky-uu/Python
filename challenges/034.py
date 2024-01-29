'''Display the following message:
        1) Square
        2) Triangle
If the user enters 1 then it should ask for length of one of its side
and diaplay the area. if they select 2, it shloud ask for the base and height
 of the triangle and display the area. if they type in anyhing else, it should
 give them a suitable error'''
message = int((input("""Enter either of two
1) Square                     
2) Triangle: """)))
if (message == 1):
    length = float(input("Enter length of the square: "))
    area = length**2
    print("Area of square is: ",area)
elif (message == 2):
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = (base * height)/2
    print("Area of triangle is: ",area)
else:
    print("Wrong Input!")
