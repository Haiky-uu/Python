# 73 two - number sum:input list l1 = [2,18,11,23,34,3,22]
# .. Write a program to find out two numbers that have sum = 45

def conv(l1:list):
    dic = {}
    for idx in range(len(l1)):
        dic[idx] = l1[idx]
    print(dic)
    c = 0

    for k,v in dic.items():
        #print(dic[k])

        first = dic[k]
        #print(first)
        for k,v in dic.items():
            if k < len(dic) -1:
                second = dic[k+1]
                #print(second)
                if ((first+second) == 45):
                    print(first,second)
def conv2(l1):
    dic = {}
    for num in l1:
        if 45-num in l1:
            print(num,45-num)
            dic[num]=45-num
    print(dic)



def main():
    l1 = [2,18,11,23,34,3,22]
    print("program")
    conv(l1)
    conv2(l1)


if __name__ == '__main__':
    main()



