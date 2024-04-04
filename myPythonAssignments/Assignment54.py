# 54 get a large list of numbers
# a = [32,43,55,11,2,3,4,5,66,33,66,7,567,89,87,54,32,12,34,567,333,256,242,121],
# sort the list and search a user given number in list using binary search technique

a = [32, 43, 55, 11, 2, 3, 4, 5, 66, 33, 66, 7, 567, 89, 87, 54, 32, 12, 34, 567, 333, 256, 242, 121]

for i in range(len(a)):
   # print(i)
    min = i
    for j in range(len(a)+1):
        if (j < min):
            min = j
print(min)