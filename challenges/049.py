
compnum = 50
value = int(input("Enter a number: "))
count = 0
while (value != compnum):
    if (value > compnum):
        print("Too high")
    elif (value < compnum):
        print("Too low")
    value = int(input("Have another guess: "))
    count += 1
print(f"Well done you took {count} attempts")


