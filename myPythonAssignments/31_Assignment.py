#Pattern print
num = 1
n = 7
for i in range(n):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()