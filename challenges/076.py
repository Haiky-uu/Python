friendList = []

print("Enter 3 Friends to the list.")
temp = 1
while(temp < 4):
    user = input(f"Enter {temp} friend to list: ")
    friendList.append(user)
    temp += 1

print(friendList)
another = input("Do you want to add another(yes/no): ")

while (another == 'yes'):
    user = input("Enter name of another friend: ")
    friendList.append(user)
    another = input("You want to add more(yes/no): ")
print(f"\nYou have added {len(friendList)} number of friends,\nThey are {friendList}")


