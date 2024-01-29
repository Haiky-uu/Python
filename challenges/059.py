import random

color = random.choice(['red','blue','green','black','yellow'])
print(color)
ans = input("Guess a color from red, blue, green, black and yellow: ")

while(ans != color):
    if (color == 'red'):
        print(f"I think you probably feel {color} right now.")
    elif (color == 'blue'):
        print(f"Can you see the complexion in {color}.")
    elif (color == 'green'):
        print(f"I don't liek {color} do you.")
    elif (color == 'black'):
        print(f"You can't see in dark why? is is because it is {color}")
    elif (color == 'yellow'):
        print(f"Sometimes i think is {color} the color of sun")
    ans = input("Try again: ")
print("Well Done!")

