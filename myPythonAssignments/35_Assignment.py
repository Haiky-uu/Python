# 35 get a number from user and check number of occurrences of a
# single digit in that number.
# (for example. Num=7888, check number of occurrences of digit 8 in number)

user = int(input("Enter a number: "))
get = str(input("Enter o search: "))
print(user)
user = str(user)
cnt = 0
for i in user:
    # print(i)
    if i == get:
        cnt += 1
print(f"Number of occurrence {cnt} of {get} number ")