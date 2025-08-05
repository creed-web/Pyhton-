import os
dir_name = 'packages'
file_name = 'file.txt'
full_path = os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)