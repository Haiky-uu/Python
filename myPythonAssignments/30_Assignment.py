#Pattern Printing
n = 10
for i in range(n):
    for j in range(i+1):
        j+=1
        print(j, end=" ")
    print()