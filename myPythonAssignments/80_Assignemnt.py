# write a function to concatenate two strings (get two strings from user and pass
# them to a function that returns concatenated string)

string1 = str(input("Enter a string: "))
string2 = str(input("Enter second string: "))


def concat(str1: str, str2: str):
    print("Your concatenated string is: ", str1+str2)


concat(string1, string2)
