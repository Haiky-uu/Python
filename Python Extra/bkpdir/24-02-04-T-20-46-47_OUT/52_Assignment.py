#52 get a string from user and write a function to return 1st non repeating character (if 1st character is not repeating then return -1)

string = input("Enter a string: ")
fnc = ''
index = -1
if (len(string) == 0):
    print("string is empty.")
for i in string:
    if string.count(i) == 1:
        fnc = i
        break
    else:
        index += 1
if (index == len(string)-1):
    print("All characters are repeating")
else:
    print("First non-repeating value is : ",fnc)