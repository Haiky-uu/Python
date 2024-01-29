
count = 0
add = 'y'

while (add == 'y'):
    invite = input("Name to add to pary list: ")
    print(f"{invite} has now been invited")
    count += 1
    add = input("Do you want to add some body else: ")
print(f"Total friends added to the list: {count}")
