food = {}
count = 0
key = 0
while(count < 4):
    count += 1
    user = input(f"Enter your {count} favourite food: ")
    key += 1
    food[key] = user
    print(f"Adding {user} item in your bucket list your bucket: {food}")

#for i in food:
print(food)
for key,item in food.items():
    print(key,item,end=" ")

a = int(input("\nDo you want to remove anything from your list: "))

if a in food:
    removed_item =food[a]
    del food[a]
    print(f"Removed item {removed_item} ")
else:
    print("wrong index")

print(food)








