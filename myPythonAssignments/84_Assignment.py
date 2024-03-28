# 84 ask user to enter a word, write a function to count number of vowels in the word

word = str(input("Enter a word: "))

def vowels(word,vowel):
    count = 0
    for let in word:
        # print(let)
        if let in vowel:
            count += 1
    print(f"vowels came in {word} {count} times ")


vowelsAll = 'aeiouAEIOU'
vowels(word,vowelsAll)