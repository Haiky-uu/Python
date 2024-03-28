# 83 ask user to enter a sentence, store sentence as list of words.
# Enter another word from user and write a function to find out number of occurrences
# of the word in the sentence

def convert(sen: str, a: list):
    for i in sen.split():
        a.append(i)
    return a

def occur(words: list, inp: str):
    count = 0
    for ele in range(len(words)):
        # print(words[ele])

            if inp == words[ele]:
                count+=1
    print(f'Word {inp} has came {count} times')


sen = input("Enter a sentence: ")
words = []
convert(sen, words)
print(words)
string = input("Enter a string: ")
occur(words, string)



