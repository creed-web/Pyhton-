import os
#this method is used so we can prevent overwriting due to write only mode

with open('example.txt','a') as file:
    file.write('Append done succesfully lads no need to worry!!')
