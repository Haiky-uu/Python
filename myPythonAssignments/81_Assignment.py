# write a function to compare two lists,
# function should return 1 if lists are same and 0 if lists are not same

list1 = [1,2,3,4]
list2 = [1,2,3,5]

def compare(l1 :list,l2: list):
    if l1 == l2:
        return 1
    return 0

def compare1(l1: list , l2: list):
    if len(l1) != len(l2):
        return 0

    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return 0
    return 1



print(compare(list1, list2))
print(compare1(list1,list2))
