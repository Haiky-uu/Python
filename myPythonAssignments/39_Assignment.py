#39 start with hard coded list say a = [12,3,34,45,88,23,45,63,3,4,69,99] and find  maximum in this list (without using python readymade function)

# using brute force
a = [12, 3, 100, 45, 88, 23, 45, 633, 3, 4, 69, 99]
new = 0
# or new = a[0]

for i in a:
    if (new < i):
        new = i
print("Your max value is: ", new)

for i in a:
    if (new > i):
        new = i
print("Your min value is: ", new)








