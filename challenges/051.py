
bottle = 10
print(f"There are \"{bottle} green bottles hanging on the wall\".")
count = 1
while (bottle != 0):
    print(f"And if 1 green bottle should accidently fall.")
    ans = int(input("How many bottles hanging on the wall?: "))
    if (ans == bottle-1):
        bottle = bottle-1
        print(f"There will be {ans} bottles hanging on he wall.")
    else:
        print("No try again!")



print("There are no more green bottles hanging on the wall.")
