'''Ask the user to type in the fiest line of a nursery rhyme and display
the length of the string. ask for a starting number and an ending number and then
display just that secion of the text (remember pyhon starts couning from 0 and not 1)'''
rhyme = input("Enter a nursury rhyme: ")
print("Rhyme is: ",rhyme,"\nLength of rhyme is: ",len(rhyme))
sNum = int(input("Enter starting number: "))
eNum = int(input('Enter ending number: '))
print("Your section is: ",rhyme[sNum:eNum],"\nLength of section is: ",len(rhyme[sNum:eNum]))

