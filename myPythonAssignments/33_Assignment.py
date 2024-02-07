"""33 Given 21 Matchsticks and 2 users, A and B (computer and user respectively).
 Users can pick matchsticks not more than four at a time.
 The one who is forced to pick the last matchstick loses."""
import random

user = input("Do you want to play game(y/n): ")
if(user == 'y'):

    print('''Game is:-
    Given 21 Matchsticks and 2 users, A and B (computer and user respectively).
 Users can pick matchsticks not more than four at a time.
 The one who is forced to pick the last matchstick loses''')

    match = 21

    #user = int(input("Enter a number to pick: "))

    while (match > 0):
        user = int(input("\nHow many matches you will pick: "))
        if(user > match):
            print("You lose")
            break
        while (user>4):
            if(user > 4):
                user = int(input("You can only pick 4 matchsticks: "))

        match -= user
        #match = match -user
        cmp = random.randint(1,4)
        print("Computer picked: ",cmp)

        if(cmp > match):
            print("Computer lose")
            break
        match -= cmp
        print("Track: ",match)

print("Bye bye...")