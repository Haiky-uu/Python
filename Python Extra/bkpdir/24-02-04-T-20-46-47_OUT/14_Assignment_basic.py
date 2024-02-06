#"14"Ask user to enter number if number is in 1s then print one, if number is in 10s then print ten if number is in 100s then print hundred if number is in 1000 print thousand. (try to implement this using if-elif-else","14_Assignmentconditional statements","conditional statements","Programming Concepts 1"
number = input("Enter number:");
 
if (len(number) == 1):
     print("Number is one's");

elif (len(number) == 2):
     print("Number is ten's");

elif (len(number) == 3):
     print("Number is hundred's");

elif (len(number) == 4):
     print("Number is thousand's");

else:
     print("Number is wrong");
exit();

