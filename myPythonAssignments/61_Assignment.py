# findout longest peak - input: l1:[3,23,25,4,5,8,2,5,6,7,9,11,3,1,0, 22,34] ---
# length of largest peak in this problem is 9

l1 = [3,23,25,4,5,8,2,5,6,7,9,11,3,1,0,22,34]
valley = []
peaks = []
ascend = False
for idx in range(len(l1)-1):
    if l1[idx]<l1[idx+1]:
        if not ascend:
            valley.append(idx)
        ascend = True
    else:
        if ascend:
            peaks.append(idx)
            ascend = False

for idx in range(len(valley)-1):
    ls = [0,0]
    if ls[0]+ls[1] < valley[idx]+valley[idx+1]:
        ls[0] = valley[idx]
        ls[1] = valley[idx+1]
print(ls)
lst = [a for a in range(ls[0],ls[1])]
print(len(lst))

print(valley)
print(peaks)
