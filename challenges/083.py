
user =input("Enter a word in upper case: ")

while (user.islower()):

    print("your input is in lower case: ", user, "Try again")
    user = input("Try again Enter a word in upper case: ")

print("good your input is in uppercase: ", user)
