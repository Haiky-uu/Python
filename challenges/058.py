import random
count = 0
for i in range(5):
    num = random.randint(1,5)
    num2 = random.randint(1,5)

    add = num + num2

    guess = int(input(f"Guess the addition of {num} and {num2}: "))
    if (guess == add):
        print("Correct")
        count +=1
    else:
        print("That was wrong")
print(f"Your score was {count}.")
