# write a function to study pass by value and pass by reference
# (write a function that accepts one variable and one list, increment
# variable inside the function by 1 and print the variable inside function and print
# variable before and after function call. inside function add 3 to all the elements of the list.
# print list inside function and before and after function call)

'''Depending on the type of object you pass in the function, the function behaves differently.
Immutable(string,integer,tuple)
 objects show “pass by value” whereas mutable(list,dict) objects show “pass by reference”.'''

def modify(var :int, list1: list):
    var = var+1
    # var+=1
    print("During_integer:", var)

    for el in range(len(list1)):
        list1[el] += 3
    print(list1)
    return var



a = 10
l1 = [1,2,3]
print('before_integer: ',a)
print('before_list: ',l1)
modify(a, l1)
print('after_integer: ',a)
print('after_list: ',l1)
'''
new_var = modify(a, l1)
print('Value can be stored: ', new_var)
print(type(new_var))
'''