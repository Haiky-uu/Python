word = input("Enter a name: ")
length = len(word)
#print(length)
num = 1
for w in word:
    pos = length - num
    #print(pos)
    letter = word[pos]
    print(letter)
    num += 1