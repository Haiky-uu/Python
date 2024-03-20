# 53 smallest difference between two numbers from two lists
# (one number from each list). Input l1: [2,4,6,8], l2:[3,10,18,19] .. Output is 1 for this example

ip1 = input("Enter 1st list:").strip().split(',')
ip2 = input("Enter 2nd list:").strip().split(',')
list1 = []
list2 = []
for i in range(len(ip1)):
    list1.append(int(ip1[i]))
    list2.append(int(ip2[i]))
print(list1,list2)
min = list1[0]-list2[0]
print(min)
for i in range(len(list1)):
    #print(i)
    nm=list1[i]-list2[i]
    if(nm<min):
        min=nm
        print(f"{list1[i]}-{list2[i]}")
        print("The difference is: ",min)
        break
else:
    print('The difference is',min)




