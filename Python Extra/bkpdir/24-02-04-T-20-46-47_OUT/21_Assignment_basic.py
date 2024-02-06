#"21","get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to browse over this list and print previous number and current number","21_Assignmentlist","loops",

a = [2,3,4,5,6,8,9,10];

for i in range(len(a)):
    #print(i);  #Printing the indexes of list
    
    #print("Previous val:",a[i-1]); #Not working prints the last val of list not null as circualr
    #print("Current val:",a[i])

    if(i == 0):
        print("Current value:",a[i]);
        print("previous value:null");
        continue;
    print("Current value:",a[i]);
    print("Previous value:",a[i-1]); 

