#"20","get a character from user and check if the character is number or vovel or conconent","20_Assignmentconditional statements","conditional statements"
value = input("Enter value:");
if (value.isalpha()):
    print("value is alpha");

    if (value == 'a' or value == 'e' or value == 'i' or value == 'o' or value == 'u'):
        print("value is a vovel");
elif(value.isdigit()):
    print("value is digit/numeric");


