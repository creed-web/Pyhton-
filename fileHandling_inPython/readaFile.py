import os

#Reading a file as an whole
with open ('example.txt','r') as file:
    scanner = file.read()

print(scanner)
