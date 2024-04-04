# 124 Walk path given by users (os.walk)
# and generate report about number of files, no of directories and size of every directory

import os

path = r'/home/viper/Documents/Python/my_python_work/Python/'

for dir, sub_dir, files in os.walk(path):
    print("\n -- Path is: ",path)
    print("Current_dir is : ",dir,)
    print("Sub_dirs: ",sub_dir,"\nAnd no of sub_dir is:",len(sub_dir))
    print("Files: ",files,"\nAnd no of files is: ",len(files))

    for filename in files:

        path = os.path.join(dir, filename)
        size = os.stat(path).st_size
        print(f"Size of {filename}: ", size)




