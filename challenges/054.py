import random

ht = random.choice(['h','t'])
#print(ht)

user = input("Enter heads or tails (h/t): ")

if (user == ht):
    print("You win")
else:
    print("Bad luck")
    print("System chosed: ",ht)

