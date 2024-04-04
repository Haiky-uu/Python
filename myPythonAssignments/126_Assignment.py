# 126 Write a program to find out duplicate files and move duplicate files to a separate folder named filesToBeArchived
import os
from filecmp import cmp
import shutil

path = './Test/moved'
print(path)
duplicate = []
for files in os.listdir(path):
    print(files)
    if_dup = False
    for class_ in duplicate:
        if_dup = cmp(path +'/'+files,path +'/' +class_[0], shallow=False)
        if if_dup:
            class_.append(files)
            break
    if not if_dup:
        duplicate.append([files])
#print(duplicate)

for dup in duplicate:
    #print(dup)
    if len(dup) > 1:
        print(dup)
        for i in dup:
            print(i)
            file = os.path.join(path,i)
            print(file)
            shutil.copy(file, './Test/Files_To_Archived')





