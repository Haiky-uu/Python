# 55 find out largest range - input: l1:[1,2,3,4,5,6,8,20,21,22,23,24,25,26,33,32,71,87,7] ------
# hint sort list in ascending order… only consider those parts that are consecutive

l1 = [1,2,3,4,5,6,8,20,21,22,23,24,25,26,33,32,71,87,7]

for ele in range(0,len(l1)-1):
    print(l1[ele])
    for ele1 in range(0,len(l1),2):
        if (l1[ele] < l1[ele1]):
            l1[ele]=l1[ele1]
