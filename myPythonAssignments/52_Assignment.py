# 52 get a string from user and write a function to return 1st non repeating character (if 1st character is not repeating then
# return -1)

'''
string = input("Enter a string:")
print("You entered: ",string)
list1 = []
for s in string:
    #print(s)
    list1.append(s)
#print(list1)

for l in range(len(list1)):
    #print(l)
    #print(list1[l+1:])
    #print(list1[:l])
    if (list1[l] not in list1[l+1:]) and  (list1[l] not in list1[:l]):
        print("first non repeating char is",list1[l])
        break
else:
    print("all are repeating")
'''
# Using function

def nonrepat(string):
    for l in range(len(string)):
        if (string[l] not in string[l+1:]) and (string[l] not in string[:l]):
            print("First Non repeating character is:",string[l])
            break
    else:
        return -1

string = input("Enter a string:")
print("You entered",string)
nonrepat(string)








