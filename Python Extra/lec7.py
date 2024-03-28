"""
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
data = f.readline() # reads single line and also reads \n at end of line which is considered newline 
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
Writing to a file 'w'/
Appending to a file 'a'
'''
f = open('./files/demo', 'w')  # writing to the file overwriting

f.write("Hello to file")  # here the data gets overwrite in the file old data gets truncated/removed
f.close()

f = open('./files/demo', 'a')  # here we are appending to the existing file where data is present already

f.write("\nhello again ")  # appending to the file existing data in file remain as it is new data gets added at the end
f.close()

f = open('./files/new_file.txt', 'w')  # this is how we can create new files if they don't exist we can also use 'a'
# for creating new files
f.write('This is new sample file')
f.close()

f = open('./files/new_file.txt', 'r+')  #(no truncate mode) this is how we read and can write to the file but pointer starts from begining of a file
# means if there is something in the file it starts overwriting from the beginning of the file
f.write('abc')
#print(f.read()) # now the pointer is at abc so it will read after c from s to e
# so here 'thi' will be 'abc' then abcs is new sample file
f.close()

f = open('./files/new_file.txt', 'w+')  # (Note. file is open in truncted mode therefore we cannot print data but can be inseted to the file)
# this is how we write and read in truncated form where the data gets deleted first
# means if there is something in the file it truncates, and then we overwrite to the file
f.write('new data')
a = f.read()
#print(a)  # it will give blank space because file is opened in truncated form but there will be data in the file
f.close()

f = open('./files/new_file.txt', 'a+')  #(No truncate mode) the file is opened in append mode so pointed is at the end of the file
# so if we try to print nothing gets printed because pointer is at the end of file
print(f.read())
f.write('\nabc')  # but file gets appended new data is added at the end of the file 
f.close()

'''
The opening modes are exactly the same as those for the C standard library function fopen().

The BSD fopen manpage defines them as follows:

 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
'''

"""

# Practice
'''list1=[]
def app(list1):
    f = open('./files/pratice.txt')
    a = f.read()
    b = a.strip().split(" ")
    for el in b:
         print(el)
         new = list1.append(el)
    return new
    print(list1)
app(list1)

def func(list1):
    count = 0
    for el in list1:
         if el == 'python.':
             count+=1
    print(count)
func(list1)
'''

























