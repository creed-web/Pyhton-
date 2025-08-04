import os

with open('example.txt','w') as file:
    file.write("Hanji namaste speaking from writinginFile.py\n") #however this method overwrites the previous information
    print(file)