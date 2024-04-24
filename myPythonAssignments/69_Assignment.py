# 69 Write a program to find number of occurrence of
# every number in the list

l1 = [1,2,3,1,4,5,11,2,6,8,2]
dic = {}

for idx in range(0,len(l1)):
    print(idx)
    if l1[idx] not in dic:
        dic[l1[idx]] = 1

    else:
        dic[l1[idx]] +=1

for k,v in dic.items():
    print('ID:',k," ",v,"Times it has came")

print(dic)

