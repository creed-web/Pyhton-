#writing and reading a file at the same time with the help of seek function
import os

with open('example.txt','r+') as file:
    file.write("Hello myself varun the king\n")
    file.write("This is a new line\n")

    #now move the file cursor to the begining to read this file
    file.seek(0)
    #now we read the content of the file
    content = file.read()
    print(content)