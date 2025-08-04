import os

#reading a file Line by Line

with open('example.txt','r') as file:
    for lines in file:
        print(lines.strip()) #here the strip function removes the newline effect generated