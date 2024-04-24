# 74 Three number sum: input list l1 = [2,18,11,23,34,3,22]
# .. Write a program to find out three numbers that have sum = 43

def dicc():
    l1 = [2,18,11,23,34,3,22]
    dic = {}
    for idx in range(0,len(l1)):
        dic[idx]=l1[idx]
    return dic


def conv(dic):
    result = []
    compliment = {}
    values = 0
    for i in range(len(dic)):
        #print(dic[i])
        for j in range(i+1,len(dic)):
           values = 43 - (dic[i] + dic[j])
           if values in compliment:
               result.append([dic[i],dic[j],values])
           else:
               compliment[dic[j]] = True

    print(result)


def conv2(dic):
    l1 = [2,18,11,23,34,3,22]
    com = {}
    var = 0
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if 43-l1[i]-l1[j] in l1:
                com[43-l1[i]-l1[j]] = [l1[i],l1[j]]
    print(var)
    print(com)


def main():
    print("Hello World")
    dic = dicc()
    print(dic)
    conv(dic)
    conv2(dic)


if __name__ == '__main__':
    main()

