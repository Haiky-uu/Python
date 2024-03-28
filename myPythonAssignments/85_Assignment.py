# 85 ask user to enter a sentence and write a function to count number of words in the
# sentence

sent = str(input("Enter a sentence:"))

def count(sent: str):
    count = 0
    for word in sent.split():
        print(word)
        count +=1
    return count

print('Number of words in sentence are: ',count(sent))

