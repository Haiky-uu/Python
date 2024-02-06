# Pattern printing program
'''

*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*

'''

# Increasing Triangle pattern program
n =7
for i in range(6):
    for j in range(i+1):
        print('*',end=' ')
    print()
# Decreasing Triangle pattern program
n =7
for i in range(n):
    for j in range(i,n):
        print('*', end=' ')
    print()