# write a program to read a text file and count the numbers of lines, words and charachters used in that file

import os

def count_lines():
    with open('example.txt','r') as file:
        line = 0
        words = 0
        charachters = 0

        for lines in file:
            line += 1
            words += len(lines.split())
            charachters += len(lines)    

    print(f'Lines: {line}')
    print(f'Words: {words}')
    print(f'Charachters: {charachters}')


count_lines()