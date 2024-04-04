
#12 Ask user to enter name, age and address and let user know if user can do voting","12_Assignmentconditional statements","conditional statements","Programming Concepts

name = input("Enter name=");
age = int(input("Enter age="));
address = input("Enter address=");

if (age < 18):
    print("Sorry ",name + "cannot vote... His age is less than required age ");
else:
    print(name + " can vote");

print("Your user is name:",name + " age:" ,str(age) + " address:",address);

