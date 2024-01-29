nums = [124, 568, 912, 346]

for num in nums:
    print(num)

user = int(input("Three a three digit number: "))

pos = nums.index(user)
pos += 1
if (user in nums):
    print(f"Number You have typed {user} is in index {nums.index(user)} and position {pos}")
else:
    print("That is not in the list")
