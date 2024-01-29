nums = []
count = 0

while (count < 3):
    num = int(input("Enter nums you want (press enter):"))
    nums.append(num)
    count += 1

print(f"You have entered {count} numbers and your list is", nums)

last = input("Do you want the last number you entered(yes/no): ")
if (last == 'no'):
    del nums[-1]
    print("Removed last number your list is: ",nums)
else:
    print("No changes done:",nums)


