#"19","get marks for a student and print grade (if < 30, fail, <50 third class, <60 second class, <70 first class, >=70 distinction, =100 then gold medal","19_Assignmentconditional statements","conditional statements"

marks = int(input("Enter marks: "));

if(marks < 30):
    print("Fail");
elif(marks < 50):
    print("Third class");
elif(marks < 60):
    print("second class");
elif(marks < 70):
    print("first class");
elif (marks >= 70):
    print("distinction");
elif (marks == 100):
    print("gold");

match marks:
    case marks < 30:
        print("Fail");
    case marks < 50:
        print("Third class");
    case marks < 60:
        print("Second class");
    case marks < 70:
        print("first class");
    case marks >= 70:
        print("distinction");
    case marks == 100:
        print("gold");
        
