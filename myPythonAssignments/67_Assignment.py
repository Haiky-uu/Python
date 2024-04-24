# 67 Write a program to find duplicate number in a
# list without using setfunction

def find(l:list):
    print("program")
    print(l)
    dict = {}
    li = []

    for i in l:
        # print(i)
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    for k,v in dict.items():
        if v > 1:
            li.append(k)

    return li


def main():
    l = [1,2,1,4,5,6,2,7]
    print(find(l))

if __name__ == '__main__':
    main()
