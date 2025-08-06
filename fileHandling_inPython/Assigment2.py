#check if a path is a file or directory
import os

path = 'example.txt'

if os.path.isfile(path):
    print(f"path {path} is a file")
elif os.path.isdir(path):
    print(f'path {path} is a directory')
else:
    print(f"the path {path} is neither a file or a directory")