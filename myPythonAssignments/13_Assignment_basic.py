#13 ,"Ask user to enter number check if number is 0 or less than 0 or greater than 0","13_Assignmentconditional statements","conditional statements","Programming Concepts 1
try:
    num = int(input("Enter any numebr:"));

    if (num < 0):
        print("Number is less than 0");
    elif (num == 0):
        print("Number is exactly what you entered i.e. 0");
    elif (num > 0):
        print("Number is greater than 0");

except:    
    print("You have entered something else that's why it is printing from else");

finally:
    print("Everything done ");

