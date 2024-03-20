'''FILE I/O
Input Output
Python can be used to perform operations on a file (read and write date)'''

'''Types Of all files

1. Text Files: .txt, .docx, .log, etc.
2. Binary Files: .mp4, .mov, .png, .jpeg, etc.

'''

'''
We have to open a file before reading or writing.

f = open('file_name','mode')

file_name       mode
sample.txt      r:read mode -- It is default mode if not given
demo.docx       w:write mode

data = f.read()
f.close()
'''

'''
print(open('./files/demo')) # checking file

f = open('./files/demo')  # opening file in variable f
print(f)     # checking file

print(type(f))  # checking type of opened file

print(f.read()) # reading file and printing o/p
#OR
data = f.read()  # reading file and storing data of file into data variable
data = f.readline() # reads single line and also \n at end so there will be space 
print(data)     # printing the contents/data of that file
print(type(data))  # tpe of content/data inside the file
f.close()   # closing the file is necessary after opening it it's a good practice or 
# anyone else can perform actions

'''

'''
Modes:-
Character   Meaning
'r'         Opens for reading (default if no mode is specified)
'w'         Open for writing, truncating/rewriting/overwriting to  the file first
'x'         Creates the new file and open it for writing
'a'         Open for writing, appending to the end of the file if it exist(No overwriting)
'b'         Binary mode Opens file in binary mode (it is not default we need to specify rb to binary files)  
't'         Text mode Opens file in text mode(it is by default we don't need to specify rt for text file)
'+'         Open a disk file for updating (reading and writing)

'''

'''
Writing to a file

'''
f = open('./files/demo', 'w')






