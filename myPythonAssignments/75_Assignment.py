# 75 read file country data and print all lines, enter filename as command line argument

import sys


def prog(file,l1):
    for line in open(file):
        print(line)
        l1.append(line)
    return l1


def main():
    print("Program")
    print("Enter argv",sys.argv)
    user = str(sys.argv[1])
    l1 = []

    print(prog(user,l1))


if __name__ == '__main__':
    main()
