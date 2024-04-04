# 125 Develop a report showing total data size, by every directory in a given location.
import os

path = r'/home/viper/Documents/Python/my_python_work/Python/'

for dir, sub_dir,files in os.walk(path):

    total_size = 0
    for filename in files:
        file_path = os.path.join(dir, filename)
        # print(file_path)
        total_size += os.path.getsize(file_path)
    print(f'Total size of {dir} : {total_size} bytes')


