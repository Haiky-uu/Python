
num = int(input("Enter a value between 10 and 20: "))
count = 1

while (num <= 10 or num >= 20):
    if(num <= 10):
        print("Too low")
    else:
        print("Too high")
    num = int(input("Try again: "))
    count += 1
print(f"Thank You. You took {count} attempts")