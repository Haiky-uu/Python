friendList = []
print("Enter 3 friends in list: ")

temp = 1

while (temp < 4):
    user = input(f"Entering {temp} friend to list: ")
    friendList.append(user)
    temp += 1

print(friendList)

another = input("Do you want to add another friend to list(yes/no): ")

while (another == 'yes'):
    user = input(f"Entering {temp} friend to list: ")
    friendList.append(user)
    temp += 1
    another = input("Do you wanna add more (yes/no): ")
print(f"You have added {len(friendList)} number of friends,\nThose are {friendList}")

person = input("Enter a name of friend from the list: ")
if (person in friendList):
    new = input(f"{person} is in index {friendList.index(person)}\nDo you want that person to come to the party (yes/no): ")

    if (new == 'no'):
        friendList.remove(person)
        print(f"Your updated friend list is: {friendList}")
    else:
        print("Your friend list remained the same: ", friendList)
else:
    print(f"{person} is not found in the friend list.")



