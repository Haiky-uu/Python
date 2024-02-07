#23 Get a number from user and revese number in other variable and print output

num = int(input("Enter a number: "))
rev = 0

while(num > 0):
#    rev = (rev * 10) + num % 10
    rev = rev * 10
    a = num % 10
    rev = rev + a
    num = num //10
print(rev)

'''
#OR

num = 239
rev = str(num)[::-1]
print(rev)
'''
