#"18","get three sides of a triangle from user and check if that is a valid triangle","18_Assignmentconditional statements","conditional statements","DS and Algorithms 1"
a = int(input("Enter a="));
b = int(input("Enter b="));
c = int(input("Enter c="));

if(a+b>c & a+c>b & b+c>a):
    print("Triangle is absolute or valid");
else:
    print("Triangle is not absolute or valid");


