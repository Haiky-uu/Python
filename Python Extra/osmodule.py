import os

print(dir(os))  # gives all functions in the module

print(os.getcwd())  # get current working directory
os.chdir("/home/viper/Documents/Python/my_python_work/myPython")  # change working directory
print(os.getcwd())

os.mkdir('test')  # creating one directory
os.makedirs('test1/new')  # creating one inside one i.e. level directory
print(os.listdir())  # lists files and folder from that dir

os.rmdir('test')  # Remove one directory
os.removedirs('test1/new')  # Remove one inside one i.e. level directories
print(os.listdir())



