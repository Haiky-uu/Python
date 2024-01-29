'''Pig latin takes first consonant of a word, moves it to the end
of the word and adds on an "ay" if the word begins with a vowel you just add "way"
 to the end.
 For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes
 aadvarkway. Create a program that will ask the user to enter a word and change
 it into Pig Latin. make sure the new word is displayed in lower case'''
word  = input("Enter a word: ")
print(word[0])
if (word[0] == ('a' or 'e' or 'i' or 'o' or 'u')):
    print(word+"way")
else:
    word = word[1:len(word)]+word[0]+"ay"
    print(word)