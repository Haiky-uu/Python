# Dictionary And sets

"""

'''
Dictionary's are built in python like tuples and lists
Dictionary's are used to store data values in key:value pairs
They are unordered , Mutable(changeable) and don't allow duplicate keys
- unordered that is there is no indexing like 0,1,2 in dictionary whilst list,tuple and string is ordered have indexes
- mutable that is we can change data inside dict and list also but not in string and tuples as they are immutable or non changeable
- we cannot create dict with same key or duplicate key like key:'value', key:'value1'
dict = {
'key':'value',
'name':'nishad',
'cgpa':8.8,
'marks':[99,55,22]
}
'''

info = {
    'key':'value',
    'name':"nishad", # value can be string
    'subjects':['python','java','c',2], # value can be list
    'topics': ('dict','sets',1), # value can be tuple
    'age':33, # value can be int
    'is_adult': True, # value can be bool
    12:11, # key can be int
    23.4:'yes', # key can be float
    ('tuple','is','key',2) : 'can be',  # key can be tuple but key cant be list
   # ['list',"can't",'be','key']: True
    True:'yes', # bool can be key

    # here dict cannot have same keys it will take value of last occurrence of that key it overrites the value of the same key
    'key1':True,
    'key1':False,
    'key1':'takes this'

}
print(info)  # Printing dict
print(type(info))  # Printing type of dict

# Accessing specific or individual values form dict
print(info["name"])
print(info['topics'])

# changing values and adding new key value pairs in dict

info['key']= 'value_changed'
print(info)
# adding new values
info['sir_name']='deshpande'
print(info)
info[55]=11
print(info)
print(info[55])

# we can create empty dict
null_dict = {

}
print("null dict:", null_dict)
null_dict['name']='new_name'
null_dict['float']=22.6
print(null_dict)

# Nested dictionaries
# dict inside dict
# we can create a key and its entire value can be a dictionary

student = {
    'name':'Nishad',
    'subjects':{
        'phy':70,
        'chem':80,
        'maths':50
    },
    'new':None
}
print(student)
print(student['subjects'])
print(student['subjects']['chem'])

# Dictionary Methods

# keys -- Returns all the keys
print(student.keys()) # Returns all keys of that dict of outer layer

# type casting
# e.g float(9) will be 9.0
print(list(student.keys()))
print(len(student))  # total value of key value pairs
print(len(list(student.keys())))

# values -- Returns all the values
print(student.values())
print(tuple(student.values()))

# Items -- Returns all (key:val) pairs as tuples
print(student.items())
print(list(student.items()))
pair = list(student.items())
print(pair[1])

# Get -- returns the key according to value
print(student.get('subjects'))  # same as print(student['subjects'])
print(student['subjects'])

'''get is same as printing value of a key so why we need get
if there is no key and we print key using normal method
without using get then it will give an error and also
next steps will not get executed but when we use .get
it will return none if there is no key and next steps
get executed try the given codes step1 and then step2'''
# Error handling using .get(), so .get() method is preferred over printing directly without .get()

'''
step 1
print("Before")
print(student['hellow'])
print("After")
print('abc')
print(2+2)
'''

'''
step 2
print("Before")
print(student.get('hellow'))
print("After")
print('abc')
print(2+2)
'''

# update - inserts the specified items to the dictionary or updates, overwrites the existing value
student = {
    'name':'Nishad',
    'subjects':{
        'phy':70,
        'chem':80,
        'maths':50
    },
    'new':None
}
# below value gets added newly
student.update({'car':'wagonr'})
#print(student)
# OR
new_dic = {
    'color':'red',
    'length':'2000'
}
student.update(new_dic)
#print(student)

# update/overwrite existing value
new_dic = {
    'name':'new_name'
}
student.update(new_dic)
print(student)

"""


# Sets in python
'''
Set is a collection of the unordered items.
Each element in the set must be unique(no duplicate values) and immutable(not changeable)
We can store int, float, string, tuple only as string and tuple both are immutable
We cannot store lists and dictionary as they are mutable or can be changed
Set are declared as dictionary's but only values no key:value pairs
'''

'''
NOTE IMP:-
Here we need to see that sets are mutable i.e. can be changed 
but values in sets cannot be mutable cannot change it should be immutable(unchangeable)
e.g
we see lists are mutable and also dict are mutable 
i.e We can add value remove value change value in lists and dicts 
that's why we cannot pass it as value to the set
so, we can only pass tuples which are immutable and strings, int etc
we are not allowed to change values in the sets 
but can add remove values

(NOTE:- Learn about hashing)
Hashing is like giving unique value to the string,tuples,lists,dict,sets etc
so when we change lists and dict which are mutable the hash changes
we cannot change sting and tuples once declared so,
their hash value dose not change and stays same forever so...
see what error you get of hash value while adding list or dict to a set 
so sets has methods to add, remove, clear, pop values/element

In an interview you need to tell sets are hashable/mutable(changeable) 
but, values in sets are un-hashable/immutable(unchangeable)
'''

collection = {1,2,3,4,'hellow','world'}
print(collection)
print(type(collection))

# Duplicate values
tuple1 = (1,2,3,3)
print(tuple)
list1 = [1,2,3,3]
print(list)

# Duplicate values are ignored in sets
set1 = {1,1,2,3,4,3,'world','hello','world',(1,4,5)}
print(set)
print(len(set1))

dict1 = {}  # This is empty dict not set
print(type(dict))

coll = set()  # Empty set; syntax
print(type(coll))

# Set Methods
coll = set()  # Empty set

coll.add(1)  # adds element to set
coll.add('hellow')
coll.add(3)
coll.add((3,5,6))
print(coll)

coll.remove(3)  # removes element from set
print(coll)
#print(coll.remove(3))

coll.pop()  # removes random element from set
print(coll)
print(coll.pop())

coll.clear()  # clears the entire set
print(coll)


set1 = {1,1,2,3,4,3,'world','hello','world',(1,4,5)}
set2 = {1,2,3,5,6,'hi','test'}
set3 = {7,8,9}
print(set1.union(set2))   # Union combines both set values and returns new values or set
print(set1.intersection(set2))  # intersection Combines common values and returns new or returns empty set if no common values found

# Questions
'''
1) Store following meanings in a python dictionary
'''

word = {'table':['a piece of furniture',' list of facts and figures'],'cat':'a small animal'}
print(word)
print(len(word))
print(word['cat'])
print(word.get('table'))
print(tuple(word.get('table')))
'''
2) You are given a list of subjects for students assume one classroom is require for 1 subject, 
how many classrooms are needed by all students ?
'''

set1 = {'python','java','c++','python','javascript','java','python','java','c++','c'}
print(len(set1))

'''
3) Wap to enter marks of 3 subjects from the user and store them in a dict start with an empty dict and add one by one
use subject name as key and marks as value
'''

subjects = {}

subjects.update({'science':65})
subjects.update({'maths':77})
subjects.update({'history':67})
print(subjects)

'''
4) figure out a way to store 9 and 9.0 as separate values in a set (you can take help of builtin data types)
'''

# first soln
set3 = {9,'9.0'}
print(set3)

#second soln
set3 = {('int',9),('float',9.0)}
print(set3)

