# 52 get a string from user and write a function to return 1st non repeating character (if 1st character is not repeating then return -1)

string = input("Enter a string: ")

index = -1
fnc = ''

if (len(string) == 0):
    print("No string is provided")

#print("String Provided: ")

for i in string:
    #print(i,end="")


    if (string.count(i)==1):
        fnc += i
        break
    else:
        index += 1

if (index == len(string)-1):
    print("\nEvery thing is repeating")
else:
    print("\nThis character is non repeating", fnc)

