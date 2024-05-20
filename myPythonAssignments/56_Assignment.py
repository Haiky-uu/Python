# move elements to last. - input l1:[2,3,5,6,7,2,4,2,6,2,3,9,7] and number given is 2 ---
# move all instances of 2 to
# end of the list ==> l1:[3,4,5,6,7,4,6,3,9,7,2,2,2,2]

l1 = [2,3,5,6,7,2,4,2,6,2,3,9,7]

# cnt = 0
# for ele in l1:
#     if ele == 2:
#         cnt+=1
#         l1.remove(ele)
#
# for ele in range(0,cnt):
#     l1.append(2)
#
# print(l1)

print(l1)
l2 = []
for idx in range(len(l1)):
    if l1[idx] == 2:
        l1.pop(idx)
        l1.append(2)
print(l1)


