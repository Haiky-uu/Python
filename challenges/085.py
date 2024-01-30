name = input("Enter your name: ")
print(name)
vowels = ['a','e','i','o','u']
count = 0
letter = 0
print("Your name and lettering is: ")
for vowel in name:

    print(vowel, letter)
    letter += 1
    if (vowel in vowels):
        count +=1
print('You got:', count, "vowels in your name")
print('Your name is: ', name)