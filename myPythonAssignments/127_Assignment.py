# 127 Write a program to move files from one directory to another (archive files)

import os
import shutil

for file in os.scandir('./Test'):
    if file.is_file():
        print(file)

        shutil.move(file, 'Test/moved/')


