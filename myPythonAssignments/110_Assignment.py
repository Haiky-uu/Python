# write a program to check working of deep copy and shallow copy
import copy

class String:

    def __init__(self,word):
        self.word = word


def main():
    pass

    word = 'ace'

    s1 = String(word)
    print(s1.__sizeof__())
    print(hex(id(s1)))

    s2 = copy.copy(s1)
    print(s2.word,hex(id(s2)))

    s3 = copy.deepcopy(s1)
    print(s3.word,hex(id(s3)))


if __name__ == '__main__':
    main()
