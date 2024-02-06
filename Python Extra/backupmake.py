# create a directory using current date timestamp
# create a backup directory using current date timestamp
# move existing output to the bkp directory

import os
import shutil
from datetime import datetime as DateTime
try:
    os.mkdir('bkpdir')
except Exception as e:
    print("Folder is present")


destination = "./bkpdir"
print(os.getcwd())

dt = DateTime.now()
print(dt)

dtStr = dt.strftime('%y-%m-%d-T-%H-%M-%S') + '_OUT'
print(dtStr)
destination = os.path.join(destination,dtStr)
print(destination)
try:
    os.mkdir(destination)
except Exception as e:
    print('Folder is present')
print(destination)

source = r'../myPythonAssignments'

files = os.listdir('../myPythonAssignments')

print(f"Total files in {source} are {len(files)}")
print('-->',files)

for f in files:
    fileName = source + '/' + f
    print(fileName)
    if(os.path.isdir(destination)):
        shutil.move(fileName,destination)
    else:
        print('cannot move files destination is empty')

